FROM tensorflow/tensorflow:1.10.1
# RUN python3
# RUN python3 -m pip install --user numpy scipy matplotlib pandas sklearn pandas_datareader
RUN python -m pip install --user keras
RUN python -m pip install --user tflearn
RUN python -m pip install --user gym
RUN python -m pip install --user textblob
RUN python -m pip install --user nltk

WORKDIR /app





