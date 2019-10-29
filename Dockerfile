FROM tensorflow/tensorflow
# RUN python3
# RUN python3 -m pip install --user numpy scipy matplotlib pandas sklearn pandas_datareader
RUN python -m pip install --user keras
RUN python -m pip install --user tflearn
RUN python -m pip install --user gym
RUN python -m pip install --user flake8

WORKDIR /app





