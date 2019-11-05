FROM alpine:3.9
WORKDIR /app
ARG TAG=1.0.5
RUN apk --no-cache add git python3 && \
    git clone https://github.com/HuobiRDCenter/huobi_Python.git && \
    cd huobi_Python && \
    git checkout ${TAG} && \
    python3 setup.py install && \
    cd .. && \
    rm -rf huobi_Python
CMD ["pwd"]