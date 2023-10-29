#!/bin/bash

# pyenvをクローンする
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# pyenv の Path を通す
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# 設定を反映させる
source ~/.bashrc

# 最新化
sudo apt update
sudo apt upgrade

# python ライブラリをインストール
sudo apt install \
build-essential libbz2-dev libdb-dev \
libffi-dev libgdbm-dev liblzma-dev \
libncursesw5-dev libreadline-dev libsqlite3-dev \
libssl-dev tk-dev uuid-dev \
zlib1g-dev

# Python 3.10をインストールする
pyenv install 3.10

# インストールされているバージョンを表示する
pyenv versions

# 3.10をデフォルトにする
pyenv global 3.10

# Pythonのバージョンを確認する
python --version

pip3 install --upgrade pip
pip3 install pipenv

# pipenv の Path を通す 
# PATH がおかしい or わからない時は whereis コマンドを使う
echo 'export PIPENV_ROOT="$PYENV_ROOT/shims/pipenv"' >> ~/.bashrc
echo 'export PATH="$PIPENV_ROOT/bin:$PATH"' >> ~/.bashrc

# 設定を反映させる
source ~/.bashrc