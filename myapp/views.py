from django.shortcuts import render

from django.http import HttpResponse

# テンプレートhtmlを読み込みするためTemplateViewをインポートする
from django.views.generic.base import TemplateView

# Create your views here.

# URLでアクセスをされたときに実際に処理される内容を以下に記述
def hello(request):
    return HttpResponse('django myapp response!!')

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
    
