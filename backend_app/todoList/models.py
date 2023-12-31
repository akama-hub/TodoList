from django.db import models

# データテーブルを作る
class todoModel(models.Model):
    # フィールドタイプ
    # https://qiita.com/KeAt/items/55fdedc8cac7c6852043
    # 公式ドキュメント: https://docs.djangoproject.com/ja//2.2/topics/db/models/
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.TextField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)

    # __str__ オブジェクトを文字列表現するためのメソッド
    # つまり、管理画面のタイトルに反映する
    def __str__(self):
        return self.title
