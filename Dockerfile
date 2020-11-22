FROM ubuntu:18.04

RUN apt-get update && apt-get -y install \
cmake \
python3.8 \
python3-pip \
build-essential \
manpages-dev

RUN pip3 install conan

COPY . /home/assignment

WORKDIR /home/assignment

ENTRYPOINT ["/bin/sh", "compilation_script.sh"]
