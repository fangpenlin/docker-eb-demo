NAME=victorlin/echoapp
VERSION=`git describe`
CORE_VERSION=HEAD

all: prepare build

prepare:
	git archive -o docker/echoapp.tar HEAD

build:
	docker build -t $(NAME):$(VERSION) --rm docker

tag_latest:
	docker tag $(NAME):$(VERSION) $(NAME):latest

test:
	nosetests -sv

push:
	docker push $(NAME):$(VERSION)
