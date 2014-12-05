FROM phusion/baseimage:0.9.15
MAINTAINER Victor Lin <hello@victorlin.me>

# install dependencies
RUN apt-get -qq update && \
    apt-get install -y \
        python \
        python-pip \
    && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN easy_install -U setuptools && \
    pip install -U pip

# add echoapp service
ADD echoapp.sh /etc/service/echoapp/run
RUN chmod +x /etc/service/echoapp/run

# install packages
ADD echoapp.tar /srv/echoapp
RUN pip install -e /srv/echoapp

VOLUME ["/var/log"]
ENTRYPOINT ["/sbin/my_init"]
EXPOSE 80
