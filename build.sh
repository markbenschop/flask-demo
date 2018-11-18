#!/bin/bash

if [ "$#" -lt 1 ]; then
    echo 'Please specify a version number'
    exit 1
fi
version=$1
echo "version : ${version} "
docker build -t flask-demo:${version}  . && \
docker tag flask-demo:${version} markbenschop/flask-demo:${version}  && \
docker push markbenschop/flask-demo:${version}
