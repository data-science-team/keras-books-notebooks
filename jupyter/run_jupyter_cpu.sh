echo "init path = "
SCRIPTPATH=$(cd "$(dirname "$0")" && pwd)
echo $SCRIPTPATH
echo "cleanup"
docker stop jupyter_cpu
docker rm jupyter_cpu
echo "docker run jupyter"
docker run -d -p 8887:8888 -v $SCRIPTPATH/jupyter_notebook_config.py:/root/.jupyter/jupyter_notebook_config.py -v $SCRIPTPATH/../:/tf/notebooks:z -e GRANT_SUDO=yes --user root --name jupyter_cpu --privileged yuryueng/jupyterconda
echo "Finished"
