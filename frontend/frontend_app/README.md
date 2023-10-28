# FrontendApp

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 16.2.0.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via a platform of your choice. To use this command, you need to first add a package that implements end-to-end testing capabilities.

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI Overview and Command Reference](https://angular.io/cli) page.


# Angular と Django の連携

## Angular 側

### 1. src/environment/proxy.config.json を作成する
```
{
    "/api": {
        "target": "http://localhost:4000",　<!-- Django のアプリケーションサーバ -->
        "secure": false,
        "changeOrigin": true,　<!-- ローカルマシンで動かすときはfalse -->
        "logLevel": "debug"　<!-- サーバの状態を確認できる -->
    }
}
```
### 2. angular.json に変更を反映する
angular.json の　architect の serve json にオプションを追加する
```
"options": {
    "browserTarget": "frontend_app:build",
    "proxyConfig": "src/environments/proxy.config.json"
},

```

### 3. Angular と Django のhttpclient 通信
+ app.module.ts に反映: HttpClientModule をインポートする
+ service を作成し、HttpClient通信を実装する


###　4. Django で Angular からのアクセスを許可する
[参考](https://qiita.com/shun198/items/9ebf19d8fd2c412396dd)

このままだと、以下のようなエラーが出るので
```
Access to XMLHttpRequest at 'http://localhost:4000/api/posts/' from origin 'http://localhost:4200' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.
```

django-cors-headers　パッケージをインストールし、Djangoのsettings.py に設定を追加
```
# corsheadersを追加
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest-framework',
    'corsheaders'
]

# corsheaders.middleware.CorsMiddlewareを追加
MIDDLEWARE = [
    # 一番上に記載
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# 自身以外のオリジンのHTTPリクエスト内にクッキーを含めることを許可する
CORS_ALLOW_CREDENTIALS = True
# アクセスを許可したいURL（アクセス元: Angular URL）を追加
CORS_ALLOWED_HOSTS = [
    'http://localhost:4200'  
]
```

