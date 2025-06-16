#!/usr/bin/env bash

set -e

run flask --app src.app db upgrade
run guiunicorn src.wsgi:app
