# URLのパターンの解析ができるように、path をインポートしておく
from django.urls import path

# views.pyが利用できるように、インポートしておく
# from . で、このパッケージの内容をインポート・読み込みする
from . import views

app_name = 'myapp'

urlpatterns = [
    # に入ってきたときの対応する関数はindex
    path('', views.index, name='index'),
    
    # path('URLの条件、パターン', 実行させる関数名, name='このURLのパターンの名称を設定' )
    path('hello/', views.hello, name='hello'),
    
    # myapp/home にアクセスされたときは、Homeクラスを利用する(TemplateView クラスを継承したクラス)
    path('home/', views.Home.as_view(), name='home'),
    
    # パスパラメータとして変数を受け取る
    path('calc/<int:num1>/<int:num2>', views.calc, name='calc')
]
