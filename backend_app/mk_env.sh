#!/bin/bash

# pyenvをクローンする
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# pyenvの環境設定に追加する
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc

# 設定を反映させる
source ~/.bashrc

# Python 3.10をインストールする
pyenv install 3.10

# インストールされているバージョンを表示する
pyenv versions

# 3.10をデフォルトにする
pyenv global 3.10

# Pythonのバージョンを確認する
python --version

pip install --upgrade pip
pip install pipenv