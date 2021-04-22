class AccuracyCalculationService:
    @staticmethod
    def acc(output, label):
        # output: (batch, num_output) float32 ndarray
        # label: (batch, ) int32 ndarray
        return (output.argmax(axis=1) ==
                label.astype('float32')).mean().asscalar()