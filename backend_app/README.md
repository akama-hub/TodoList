# Django × Angular で Todo アプリを作ってみる
以下、勉強のアウトプット用にメモを残していく

#  目次

- [Django × Angular で Todo アプリを作ってみる](#django--angular-で-todo-アプリを作ってみる)
- [目次](#目次)
  - [Django の概要](#django-の概要)
    - [wsgi.py](#wsgipy)
    - [settings.py](#settingspy)
  - [Django のインストール](#django-のインストール)
  - [プロジェクトの作成](#プロジェクトの作成)
  - [アプリの作成](#アプリの作成)
  - [データベースマイグレーション](#データベースマイグレーション)
  - [アプリケーションの実行](#アプリケーションの実行)
- [Django で Database を作成する流れ](#django-で-database-を作成する流れ)
  - [1. model に作成したいデータテーブルの作成](#1-model-に作成したいデータテーブルの作成)
    - [1-1-1. そもそもモデルとは・・・](#1-1-1-そもそもモデルとは)
    - [1-1-2. モデルの作成](#1-1-2-モデルの作成)
    - [1-1-3. settings.pyを更新](#1-1-3-settingspyを更新)
  - [1-1-4. model から migrations ( 更新差分 ) を作成](#1-1-4-model-から-migrations--更新差分--を作成)
  - [1-1-5. migrations を元に Database を作成・更新](#1-1-5-migrations-を元に-database-を作成更新)
  - [1-1-6. admin ページへのアクセス手順](#1-1-6-admin-ページへのアクセス手順)
    - [1-2. そもそもビューとは・・・](#1-2-そもそもビューとは)
  - [1-2-1. Function Based View](#1-2-1-function-based-view)
  - [1-2-2. Class Based View](#1-2-2-class-based-view)
  - [1-2-3. Class Based View 継承を使うメリット](#1-2-3-class-based-view-継承を使うメリット)
    - [1-2-4. 汎用ビューの種類と特徴（簡易版）](#1-2-4-汎用ビューの種類と特徴簡易版)
    - [1-2-5. ミックスイン](#1-2-5-ミックスイン)

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
pyrenv × pipenv で環境構築

```$ bash mk_env.sh```を実行する

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


# Django で Database を作成する流れ

## 1. model に作成したいデータテーブルの作成

「Django ORM（Object-Relational Mapper）」という仕組みが備わっていてDBのレコードをモデルオブジェクトとして扱える

### 1-1-1. そもそもモデルとは・・・
[参照：Django のモデルについて](https://note.com/saito_pythonista/n/n920bbc48c8fd)

HTMLファイルに埋め込むためのデータをDB（データベース）とやり取りし、ビュー（views.py）に返す

[1-2. そもそもビューとは・・・](###-1-2.-そもそもビューとは・・・)

![](https://assets.st-note.com/production/uploads/images/47823670/picture_pc_bdbcecb609fdc56619fd3bbf524d814e.jpg?width=800)

### 1-1-2. モデルの作成
```
from django.db import models

class test(models.Model):
    test_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
```

### 1-1-3. settings.pyを更新
```
INSTALLED_APPS = [
    'test.apps.TestConfig', # 追加
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

## 1-1-4. model から migrations ( 更新差分 ) を作成
```
$ python3 manage.py makemigrations test

# 以下は結果
Migrations for 'test':
  test/migrations/0001_initial.py
    - Create model test
```

「test/migrations/0001_initial.py」が新しく作成される

SQL の確認方法

```
$ python3 manage.py sqlmigrate test 0001

# 以下は結果
BEGIN;
--
-- Create model test
--
CREATE TABLE "test_test" ("test_id" integer NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL);
COMMIT;
```

## 1-1-5. migrations を元に Database を作成・更新
```
$ python3 manage.py migrate

# 以下は結果
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions, test
Running migrations:
  Applying test.0001_initial... OK
```


## 1-1-6. admin ページへのアクセス手順
まず、adminページのログインユーザの作成する

```
$ python3 manage.py createsuperuser

# 以下は結果
Username:
Email address:
Password:
Password (again):
Superuser created successfully.
```

admin.py の更新

変更箇所：MyProject\test\admin.py (「# Register your models here.」を目印)




### 1-2. そもそもビューとは・・・
[参照：Django のビューについて](https://note.com/shingo_takagi/n/nf7e84d40f23e)

![](https://assets.st-note.com/production/uploads/images/47439170/picture_pc_cb71b94910064eb7ab09ab298298875f.png?width=2000&height=2000&fit=bounds&format=jpg&quality=85)

Viewは、WebアプリにHTTPリクエストを送り、レスポンスが返るまでのフローの中で
+ 表示するHTMLファイルを選択する
+ 表示する内容をカスタムするための変数を準備する
+ 変数をHTMLファイルの指定位置に埋め込み、表示ページを完成させる

## 1-2-1. Function Based View

引数に request を使った例
``` 
from django.shortcuts import render

def toppage(request):
    if request.method == GET:
        user = request.user
        # アクセス先設定
        return render(request, 'toppage.html, {'pk': user.pk})
```

Webアプリ開発では、「表示ページの状態」を戻り値にセットすることが多く、renderメソッドのなかでrequestを使う

その他に、HTMLに埋め込みたいデータを作成するのに必要な引数も受け取れる。その際、タプルで受け取るものは*args、辞書型で受け取るものは**kwargsに格納

## 1-2-2. Class Based View

Class Based View の引数には継承するクラスを使用
``` 
from django.shortcuts import render
from django.views import View

class toppage(View):
    def get(self, request):
        user = self.request.user
        # アクセス先設定
        return render(request, 'toppage.html, {'pk': user.pk})
```

Function Based View との違い
+ 継承用クラスのインポートが追加が必要
+ クラス定義の記述が必要
+ 対象のリクエストメソッドをdefで宣言
+ defの引数にselfが必要
+ 変数の利用にはselfの接頭辞が必要

## 1-2-3. Class Based View 継承を使うメリット
共通で使いたい定義を持つベースビューを自作し、クラス宣言文の()内に継承元として記述することで継承ができ、継承元のすべての記述を引き継ぐことができる

```
from django.views.generic import TemplateView
from .models import Post

class TemplateBaseView(TemplateView):
    def get_context_data(self, **kwargs):
        # super -> 親クラスのメソッド呼びだし
        context = super().get_context_data

        posts = Post.objects.all().order_by('-created_at')
        context['posts'] = posts
        return context

class ToppageView(TemplateBaseView):
    template_name = 'toppage.html'

class InfopageView(TemplateBaseView):
    template_name = 'toppage.html'
```

### 1-2-4. 汎用ビューの種類と特徴（簡易版）
+ TemplateView
  + HTML ファイルのページ表示用
  + template_name に表示させたいファイル名をtemplateディレクトリから選択
  ```
  from django.views.generic import TemplateView

  class IndexView(TemplateView): 
     template_name = 'index.html'
  ```
+ CreateView
  + 新しいモデルオブジェクトを作成する
    + template_name
    + 作成先モデル
    + 使用フィールド
    + 作成成功時のリダイレクトURL

  ```
  from django.views.generic import CreateView
  from django.urls import reverse_lazy
  from .models import Contact

  class ContactCreateView(CreateView):
     template_name = 'contact/create.html'  
     model = Contact
     fields = ['title', 'body']
     success_url = reverse_lazy('sample_app:index')
  ```

+ UpdateView
  + 既存のモデルオブジェクト情報を変更・更新する
    + HTMLファイルの表示
    + ユーザーが入力するフォームの自動生成
    + フォームへの入力情報で既存のモデルオブジェクト

    ただし、更新できるのはURLから特定される１つのオブジェクトのみ

  ```
  from django.views.generic import UpdateView
  from django.urls import reverse_lazy
  from .models import BoardPost

  class BoardPostUpdateView(UpdateView):
     template_name = 'board_post/update.html'  
     model = BoardPost
     fields = ['title', 'body']
     success_url = reverse_lazy('sample_app:index')
  ```

+ DeleteView
  + 既存のモデルオブジェクトを削除する
    + HTMLファイルの表示
    + フォームへの入力情報で既存のモデルオブジェクト

  ```
  from django.views.generic import DeleteView
  from django.urls import reverse_lazy
  from .models import BoardPost

  class BoardPostDeleteView(DeleteView):
     template_name = 'board_post/update.html'        #3点の記述が必要
     model = BoardPost
     success_url = reverse_lazy('sample_app:index')
  ```

+ ListView
  + 複数データを取得する
    + HTMLファイルの表示
    + 同一モデルのオブジェクトの複数取得
    + ページ送りで確認可能な表示機能の実装

  ``` 
  from django.views.generic import ListView
  from .models import BlogPost

  class BlogPostListView(ListView):
     template_name = 'blog_post/list.html'    #3点の記述が必要
     model = BlogPost
     context_object_name = 'blog_posts'       #ここは任意。書かなければ{{ object_list }}で呼び出し可能
     paginate_by = 10
  ```

+ DetailView
  + 既存のモデルオブジェクト1つを取得する
    + HTMLファイルの表示
    + 特定オブジェクトの取得

  ```
  from django.views.generic import DetailView
  from .models import BlogPost

  class BlogPostDetailView(DetailView):
     template_name = 'blog_post/detail.html'    #2点の記述が必要
     model = BlogPost
     context_object_name = 'blog_post'
  ```

「Django ORM（Object-Relational Mapper）」という仕組みが備わっていてDBのレコードをモデルオブジェクトとして扱える

### 1-2-5. ミックスイン
+ LoginRequiredMixin
  + ログインユーザーでないとアクセスできない制限をかける

つまり、ログインしていないユーザーがアクセスした際にはページ表示させず、ログインページにリダイレクトさせる

ただし、リダイレクト先のログインURLは/accounts/loginとなっている必要がある

+ UserPassesTestMixin
  + 制限をカスタムできる
    + 制限の掛け方は、def test_func(self):という関数を定義し、その中でreturnに変数をセット

このセットした変数がFalseの場合にアクセス制限が機能し、アクセスしたユーザーにはstatus code 403エラーのページを表示させる動作をする

```
from django.views.generic import DetailView
from .models import CustomUser
from django.contrib.auth.mixins import UserPassesTestMixin

class Mypage(UserPassesTestMixin, DetailView):    #Mixin記述
   template_name = 'accounts/mypage.html'
   model = CustomUser
   context_object_name = user
   
   def test_func(self, request, **kwargs):
       # アクセス制限対象を定義（今回はログインユーザーと、マイページの所有者が同じか確認）
       login_user = self.request.user
       mypage_owner = super().get_context_data()
       
       # 戻り値がTrueの時のみ許可
       return (login_user == mypage_owner)         
```