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
    path('calc/<int:num1>/<int:num2>', views.calc, name='calc'),

    # コメントの入力画面を表示するURLを設定する
    # localhost/myapp/comment_create で実行される
    # as_view() メソッドで、レスポンスが返せるように処理をする
    path('comment_create', views.CommentCreateView.as_view(), name='comment_create'),

    # コメントの一覧表示用のURLを設定
    path('comment_list', views.CommentListView.as_view(), name='comment_list'),
    
    # 復習用：internetacademy/ にアクセスされたら、テンプレートのHTMLを読み込んで表示する
    # <汎用ビュークラス名>.as_view() : 指定のクラスをview関数として実行することができる
    path('internetacademy', views.Sample.as_view()),
]
