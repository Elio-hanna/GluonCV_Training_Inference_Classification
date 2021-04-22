import time
import os

from mxnet import gluon, init, autograd
from mxnet.gluon.data.vision import datasets
from application.training_module.services import model_manipulation_service,accuracy_calculation_service,data_transformation_service,model_creation_service
from application.path.services.path_service import PathService
from domain.models.path import Path

class TrainModel:
    def __init__(self):
        path = PathService()
        self.path: Path = path.get_paths()

    def create_and_train(self, model_name: str, batch_size: int, learning_rate: float, epochs: int):
        """
        Create a ModelCreationService and Train it
        :param model_name: model name
        :param batch_size: size of the batch
        :param learning_rate: learning rate to be used
        :param epochs: nb of epochs to train the model
        :return: 
        """
        model = model_creation_service.ModelCreationService()
        acc = accuracy_calculation_service.AccuracyCalculationService()
        save_model = model_manipulation_service.ModelManipulationService()
        # datasets
        try:
            cifar_train = datasets.CIFAR10(train=True)
            X, y = cifar_train[0:10]
        except Exception as ex:
            raise ex
        # transform image
        try:
            transform = data_transformation_service.DataTransformationService()
            transformer = transform.data_transformation()
            cifar_train = cifar_train.transform_first(transformer)
            # train data
            train_data = gluon.data.DataLoader(
                cifar_train, batch_size=batch_size, shuffle=True)
            cifar_valid = gluon.data.vision.CIFAR10(train=False)
            valid_data = gluon.data.DataLoader(
                cifar_valid.transform_first(transformer),
                batch_size=batch_size)
        except Exception as ex:
            raise ex
        # build model
        try:
            net = model.create_model()
            net.initialize(init=init.Xavier())
            softmax_cross_entropy = gluon.loss.SoftmaxCrossEntropyLoss()
        except Exception as ex:
            raise ex
        try:
            trainer = gluon.Trainer(net.collect_params(), 'sgd', {'learning_rate': learning_rate})
            for epoch in range(epochs):
                train_loss, train_acc, valid_acc = 0., 0., 0.
                tic = time.time()
                for data, label in train_data:
                    # forward + backward
                    with autograd.record():
                        output = net(data)
                        loss = softmax_cross_entropy(output, label)
                    loss.backward()
                    # update parameters
                    trainer.step(batch_size)
                    # calculate training metrics
                    train_loss += loss.mean().asscalar()
                    train_acc += acc.acc(output=output, label=label)
                # calculate validation accuracy
                for data, label in valid_data:
                    valid_acc += acc.acc(net(data), label)
                print("Epoch %d: loss %.3f, train acc %.3f, test acc %.3f, in %.1f sec" % (
                    epoch, train_loss / len(train_data), train_acc / len(train_data),
                    valid_acc / len(valid_data), time.time() - tic))
        except Exception as ex:
            raise ex
        try:
            save_model.save_model(net, os.path.join(self.path.model_dir, model_name))
        except Exception as ex:
            raise ex
