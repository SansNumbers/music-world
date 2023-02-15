FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
  apt-get install -y python3-pip python3-dev netcat-openbsd

WORKDIR /code
COPY . /code/
RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod a+x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
