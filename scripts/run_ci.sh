#!/bin/bash

set -e

docker compose up --build --detach

tox
