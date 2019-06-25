#!/bin/bash

if [[ ! $(which docker) ]]; then
  echo "Docker must be installed. Exiting"
fi

openfaas_repository="https://github.com/openfaas/faas"

docker swarm init

if [[ ! $(which faas) ]]; then
    mkdir -p faas
    pushd faas
    git clone "${openfaas_repository}" .
    ./deploy_stack.sh --no-auth
    curl -sL https://cli.openfaas.com | sudo sh
    popd
    rm -rf faas
fi

faas build && faas deploy

