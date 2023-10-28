# Django × Angular で Todo アプリを作ってみる

## Django の概要

### wsgi.py
+ urls.py や models.py などファイル間の中間役の役割

### settings.py
+ BASE_DIR: ルートファイルを示す
+ SECRET_KEY: Django用のプロジェクトキー
+ DEBUG: ブラウザ上にエラーを表示するか
    + 開発中はTrue, 後悔するときはFalse
+ ALLOWED_HOSTS: 外部のWebサーバのIPなど
+ INSTALLED_APPS: Djangoのアプリ
+ MIDDLEWARE: 処理をする際に間に入ってくれるもの、セッションを管理するもの
+ ROOT_URLCONF: ブラウザでURLをたたいた時に最初に呼び出すファイルを指定する
+ TEMPLATES: htmlファイルの所在を指定する
+ WSGI_APPLICATION: wsgi.pyの場所を指定
+ DATABASES: データベースの指定
+ AUTH_PASSWORD_VALIDATORS: パスワードのバリエーション管理

## Django のインストール
``` 
$ pip install django
$ pip install djangorestframework
$ pip install django-filter
$ pip install django-cors-headers
```

## プロジェクトの作成
```
$ python3 -m django startproject プロジェクト名
```

## アプリの作成
``` 
$ cd プロジェクト
$ python3 manage.py startapp アプリ名
```

## データベースマイグレーション
```
python3 manage.py migrate
```

## アプリケーションの実行
```
python3 manage.py runserver 0.0.0.0:4000
```

