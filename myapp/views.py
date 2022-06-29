from django.shortcuts import render

from django.http import HttpResponse

# テンプレートhtmlを読み込みするためTemplateViewをインポートする
from django.views.generic.base import TemplateView

# テーブルにレコードを追加する機能を持った汎用ビュー CreateViewをインポート
from django.views.generic import CreateView

# テーブルに登録されているレコードを一覧表示する機能を持った汎用ビュー ListViewをインポート
from django.views.generic import ListView

# urlを逆引き(名前からURLを解析する)ための関数をインポート
from django.urls import reverse_lazy

# Comment モデルをインポート
from .models import Comment

# CommentForm クラスをインポート
from .forms import CommentForm

# Create your views here.

# URLでアクセスをされたときに実際に処理される内容を以下に記述
def hello(request):
    return HttpResponse('<h1 style="color: orange;">django myapp response!!</h1>')

# myapp/homeにアクセスされたとき用のクラスベースのビューメソッドを作成
# テンプレートをりようするため、TemplateView クラスを継承する
class Home(TemplateView):
    # template_name のメンバ変数を設定することで、
    # 利用するテンプレートhtmlを特定する
    # settings.py で初期設定した、templatesディレクトリの中からパスを探す
    template_name = 'myapp/home.html' # templates/myapp/home.html

def index(request):
    return HttpResponse('localhost/myapp foobar')

def calc(request, num1, num2):
    # 受け取った2つの変数を足し算する
    ret = str(num1) + '+' + str(num2) + '=' + str(num1 + num2)
    return HttpResponse(ret)
    
# Commentモデルのデータをデータベースに保存すすための機能を持ったビュー
# CommentCreateView を作成する
class CommentCreateView(CreateView):
    model = Comment # Commentモデルのデータを作るので、modelにCommentを指定
    form_class = CommentForm # 利用するフォームのクラスを指定する
    template_name = 'myapp/comment_create.html' # 表示HTMLを指定

    # データベースへのレコードの追加が成功した後に表示するurl
    success_url = reverse_lazy('myapp:home') # myapp アプリケーションに設定されているname という名前のURLに遷移する

# Commentモデルのデータを一覧表示するViewを作成
# 汎用ビューのListViewを継承しておく
class CommentListView(ListView):
    model = Comment # どのモデルのデータを表示するか
    template_name = 'myapp/comment_list.html'
