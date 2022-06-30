from django import forms
from .models import Goods
 
class GoodsCreateForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ('name', 'management_code', 'price', 'release_date', 'release_flag', 'description', 'image')

# 更新画面用のフォームクラス
class GoodsUpdateForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ('name', 'management_code', 'price', 'release_date', 'release_flag', 'description', 'image')
