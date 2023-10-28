# TodoList

## Overview

実装環境
```
|--- docker-compose.yml          # Docker-compose本体
    |---.gitignore               # git対象外用
    |---frontend
        |---Angular
    |---backend
        |---Django
            |---Dockerfile       # Dockerfile
            |---requirements.txt # pipでインストールするリスト
            |---.env             # django用の環境変数
        |---Postgres
            |---.env             # mysql用の環境変数
            |---init.sql         # DB起動時(初回のみ)に流すスクリプト
```


本番環境
```
./WORKDIR
    |--- docker-compose.yml      # Docker-compose本体
    |---.gitignore               # git対象外用
    |---frontend
        |---Angular
        |---nginx
            |---nginx.conf       # nginxの設定ファイル
            |---uwsgi_params     # uwsgi用パラメータ
    |---backend
        |---Django
            |---Dockerfile       # Dockerfile
            |---requirements.txt # pipでインストールするリスト
            |---.env             # django用の環境変数
        |---Postgres
            |---.env             # Postgres用の環境変数
            |---init.sql         # DB起動時(初回のみ)に流すスクリプト
```

## Web Server (frontend-app)
Angular アプリケーションを Nginx サーバ上にデプロイ

## Application Server (backend-app)
Django アプリケーションを uWSGI サーバ上にデプロイ

## Database
Postgres

