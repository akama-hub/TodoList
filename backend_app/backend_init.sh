#!/bin/bash

# postgresql を使うためのライブラリpsycopg2-binaryをインストールするために必要なパッケージ
sudo apt-get install libpq-dev

pipenv sync
# pipenv install -r ./requirements.txt
pipenv shell