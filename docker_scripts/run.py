import docker
import os
client = docker.from_env()
client2 = docker.from_env()

currentdir = os.path.abspath(os.getcwd())

ports = {'8000/tcp': ('0.0.0.0', 8000)}
vol = currentdir + '/training_api/src'
volume = {vol: {'bind': '/main', 'mode': 'rw'}}
client.containers.run('classification_training_api', remove=True, ports=ports, volumes=volume,tty=True, stdin_open=True, detach=True)

ports2 = {'4343/tcp': '4343'}
vol2 = currentdir + '/inference_api/src'
volume2 = {vol2: {'bind': '/main', 'mode': 'rw'}}
client2.containers.run('classification_inference_api', remove=True, ports=ports2, volumes=volume2,tty=True, stdin_open=True, detach=True)

print("classification_training_api is Ready")
print("classification_inference_api is Ready")