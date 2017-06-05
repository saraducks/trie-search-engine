FROM python:3.5

MAINTAINER saranya vijay

RUN apt-get update -y 

RUN apt-get install -y git  python-pip python-dev build-essential

COPY . /trie-search-engine

WORKDIR ["/trie-search-engine"]

RUN pip install flask

ENTRYPOINT ["python"]

CMD["/trie-search-engine/dictionary_webapp/trieflaskapp.py", "-p:8500"]
