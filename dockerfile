FROM python:2.7

MAINTAINER saranya vijay

RUN apt-get update -y 

RUN apt-get install -y git  python-pip python-dev build-essential

RUN pip install -r https://github.com/saraducks/trie-search-engine/blob/master/requirements.txt

COPY . /dictionary_webapp

EXPOSE 8500

ENTRYPOINT ["python"]

WORKDIR ["/dictionary_webapp"]

CMD["trieflaskapp.py", "-p:8500"]
