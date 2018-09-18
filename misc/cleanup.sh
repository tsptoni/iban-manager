#!/usr/bin/env bash

#We build the docker image each time because it's not done
#when running docker-compose up.
# This is to avoid running the cleaner each time we do a docker-compose up
docker build -f ../compose/cleaner/Dockerfile -t insafe_cleaner_1 ..

docker run --rm -v /var/run/docker.sock:/var/run/docker.sock insafe_cleaner_1
