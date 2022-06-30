from django.shortcuts import render

from django.views import generic
from .forms import GoodsCreateForm

from .forms import GoodsUpdateForm

# リダイレクトを実行するためのモジュールをインポートしておく
from django.http import HttpResponseRedirect

# from .forms import GoodsCreateForm, GoodsUpdateForm, ImageSizeLimitationForm
 
# Goodsモデルが使えるようにインポート
from .models import Goods

class GoodsCreate(generic.CreateView):
    form_class = GoodsCreateForm
    template_name = 'crud/goods_create.html'
    success_url = '/crud/goods_create' # レコード保存に成功したらこのurlにリダイレクトする

class GoodsList(generic.ListView):
    model = Goods
    template_name = 'crud/goods_list.html'
 
class GoodsDetail(generic.DetailView):
    model = Goods

class GoodsUpdate(generic.UpdateView):
    model = Goods
    form_class = GoodsUpdateForm
    template_name = 'crud/goods_update.html'
    success_url = '/crud/goods_list'

# 論理削除(削除フラグを切り替える)のViewクラス
class CustomDeleteView(generic.DeleteView):
    model = Goods
    template_name = 'crud/goods_delete.html'
    success_url = '/crud/goods_list'
    
    # 削除の処理をオーバーライドする
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.custom_delete()
        return HttpResponseRedirect(success_url)


# 物理削除(レコード自体を削除する)のViewクラス
class GoodsDelete(generic.DeleteView):
    model = Goods
    template_name = 'crud/goods_delete.html'
    success_url = '/crud/goods_list'
