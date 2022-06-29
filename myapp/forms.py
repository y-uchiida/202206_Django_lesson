# ユーザー入力の内容を受付けるためのWebフォーム用のクラスを作成していく

from django import forms
from .models import Comment

# Comment モデル用のフォームを作成 
class CommentForm(forms.ModelForm):
    class Meta: # Metaクラスで、連携するモデルと入力欄を表示する項目を指定
        model = Comment
        fields = ('title', 'author', 'text')

