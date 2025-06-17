#!/usr/bin/env bash

set -e

run flask --app src.app db upgrade
run guiunicorn src.wsgi:app 

            0     1      2
lista = ["stone", ", item2]

indice = ramdom.randint(0,2)

lista[indice]