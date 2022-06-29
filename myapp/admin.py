from django.contrib import admin

# 管理画面に登録するモデルのクラスをインポートしておく
from .models import Comment

# Register your models here.

# 管理画面にComment クラスを登録する
admin.site.register(Comment)
