#!/usr/bin/env bash

# https://github.com/pypa/virtualenv/issues/1029
#set -eou pipefail
set -eo pipefail

library_path=lib/ansible/modules/system
project=$(pwd)
module=gsettings.py
args=${1:-${project}/args.json}

function log() {
  echo "**** $@"
}

cd ../ansible

log "Activating virtual environment"
. venv/bin/activate

log "Environment setup"
. hacking/env-setup

ln -fs ${project}/${module} ${library_path}/${module}

python ${library_path}/${module} ${args}
