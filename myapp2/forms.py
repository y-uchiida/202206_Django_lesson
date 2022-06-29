from django import forms
from .models import StaffInformation, Staff

# 従業員の詳細情報を作成するフォーム
class StaffInformationForm(forms.ModelForm):
    class Meta:
        model = StaffInformation
        fields = ('staff_name','email', 'address', 'birthday', 'hire_date', 'at_desk')

# 従業員の基本情報を作成するフォーム
class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('name', 'information')
