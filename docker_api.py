#pip install docker
# Go to http://containertutorials.com/py/docker-py.html
import docker
#cli = docker.APIClient(base_url='tcp://uls-ep-swtools-03.wdc.com:2375', tls=False)
cli = docker.APIClient(base_url='tcp://uls-ep-essd25:2375', tls=False)
print cli.containers()
container = cli.create_container(image='ubuntu:latest', command='/bin/sleep 30')
print container
q = cli.start(container['Id'])
cli.commit(container['Id'], repository='dummy/test',
          tag='version1')
