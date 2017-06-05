FROM python:3.5

MAINTAINER saranya vijay

RUN apt-get update -y 

RUN apt-get install -y git  python-pip python-dev build-essential

COPY . /trie-search-engine

EXPOSE 8500

ENTRYPOINT ["python"]

WORKDIR ["/trie-search-engine"]

RUN pip install requirements.txt

CMD["/dictionary_webapp/trieflaskapp.py", "-p:8500"]
