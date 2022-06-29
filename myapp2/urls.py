# URLのパターンの解析ができるように、path をインポートしておく
from django.urls import path

# views.py をインポート
from . import views

app_name = 'myapp2'

urlpatterns = [
	path('staff_information_create/', views.StaffInformationCreateView.as_view(), name='staff_information_create'),
    path('staff_create/', views.StaffCreateView.as_view(), name='staff_create')
]
