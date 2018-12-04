#pip install docker from concurrent.futures import ThreadPoolExecutor
# https://medium.com/statuscode/prototyping-a-parallel-computing-cluster-using-docker-25ea836a269b
from concurrent.futures import ThreadPoolExecutor
import docker
import random
def fun(message, client):
    container = client.containers.run("luv_test:latest", environment=["var=%s" % message], detach=True, remove=True)
    logs = container.logs()
    for line in container.logs(stream=True):
        print (line.strip())

client1 = docker.DockerClient(base_url='tcp://uls-ep-essd25.wdc.com:2375', tls=False)
client2 = docker.DockerClient(base_url='tcp://uls-ep-essd26.wdc.com:2375', tls=False)
messages= ["c4ca4238a0b923820dcc509a6f75849b", "c4ca4238a0b923820dcc509a6f758491", "c4ca4238a0b923820dcc509a6f75849c", "c4ca4238a0b923820dcc509a6f75849d", "c4ca4238a0b923820dcc509a6f75849b", "c4ca4238a0b923820dcc509a6f758491", "c4ca4238a0b923820dcc509a6f75849c", "c4ca4238a0b923820dcc509a6f75849d", "c4ca4238a0b923820dcc509a6f75849b", "c4ca4238a0b923820dcc509a6f758491", "c4ca4238a0b923820dcc509a6f75849c", "c4ca4238a0b923820dcc509a6f75849d"]
pool = ThreadPoolExecutor(50)
clients = [client1, client2]

for my_message in messages:
    future = pool.submit(fun, (my_message),random.choice(clients))