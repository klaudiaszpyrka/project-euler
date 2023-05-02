FROM python:3.8
RUN pip3 install jupyter
RUN pip3 install --upgrade jupyterlab
WORKDIR /notebooks
CMD jupyter notebook --port=8888 --ip=0.0.0.0 --allow-root