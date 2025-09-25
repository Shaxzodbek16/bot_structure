#!/bin/bash

# shellcheck disable=SC2155
export PYTHONPATH="$(pwd)"

python app/server/main.py
