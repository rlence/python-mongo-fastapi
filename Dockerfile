FROM python:3.10.5

# Install dockerize
ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# Create required dirs
RUN mkdir /var/log/back
# RUN mkdir /app

# Set /app as workdir
WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt