echo "init path = "
SCRIPTPATH=$(cd "$(dirname "$0")" && pwd)
echo $SCRIPTPATH
echo "cleanup"
docker stop jupyter_enjoyds_gpu
docker rm jupyter_enjoyds_gpu
echo "docker run jupyter_enjoyds_gpu"
docker run --runtime=nvidia -d -p 8887:8888 -v $SCRIPTPATH/jupyter_notebook_config.py:/root/.jupyter/jupyter_notebook_config.py -v $SCRIPTPATH/../:/tf/notebooks:z -e GRANT_SUDO=yes --user root --name jupyter_enjoyds_gpu --privileged yuryueng/jupyterconda_gpu
echo "Finished"
