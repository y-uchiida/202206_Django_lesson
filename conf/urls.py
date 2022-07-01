"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# HtmlResponse を返すためのモジュールをインポート
from django.http import HttpResponse

# プロジェクト全体の設定情報を読み込みするための設定
from django.conf import settings

# スタティックURLを設定するためのモジュールをインポート
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # myappのURL設定を利用できるようにする
    # path('URLの条件、パターン', include('条件に一致したときに処理を引き渡すファイル') )
    # localhost/myapp/... にアクセスされたら、それ以降の内容をmyapp/urls.pyのパスとして解釈させる
    path('myapp/', include('myapp.urls')),

    path('myapp2/' , include('myapp2.urls')),
    
    # crud のアプリケーションの内容へ処理を引き渡す
    path('crud/', include('crud.urls')),
    
    # ユーザー認証用の機能を持たせたアプリケーションへ処理を引き渡す
    path('accounts/', include('accounts.urls'))
    
]

# 開発環境などであれば、スタティックURLを利用できるようにする
# /media/... のURLにアクセスされたら、 Djangoのプロジェクトのmedia ディレクトリの内容を参照するように関連付けを設定する
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)
