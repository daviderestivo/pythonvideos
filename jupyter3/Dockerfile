# Copyright (c) Davide Restivo.
# Distributed under the terms of GNU General Public License v3.0

FROM ubuntu:zesty

MAINTAINER Davide Restivo <davide.restivo@yahoo.it>

USER root

# Install all OS dependencies for fully functional notebook server
RUN apt-get update && apt-get install -yq python3 \
    python3-pip \
    emacs \
    git \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install jupyter paramiko netmiko

CMD exec jupyter notebook --allow-root --NotebookApp.token='' > /var/log/jupyter.log 2>&1
