from django.views.generic import CreateView, DetailView, UpdateView, FormView, ListView
from django.urls import reverse_lazy
from .models import StaffInformation, Staff
from .forms import StaffInformationForm, StaffForm

# 社員の詳細情報を作成するための画面のビュー
class StaffInformationCreateView(CreateView):
    model = StaffInformation
    form_class = StaffInformationForm
    template_name = 'myapp2/staff_information_create.html'
    success_url = reverse_lazy('myapp:home')

# 社員の基本情報を作成するための画面のビュー
class StaffCreateView(CreateView):
    model = Staff
    form_class = StaffForm
    template_name = 'myapp2/staff_create.html'
    success_url = reverse_lazy('myapp:home')

# 社員の基本情報を一覧表示する画面のビュー
class StaffListView(ListView):
    model = Staff
    template_name = 'myapp2/staff_list.html'

# 社員の編集画面のビュー
class StaffUpdateView(UpdateView):
    model = Staff
    form_class = StaffForm
    template_name = 'myapp2/staff_update.html'
    success_url = reverse_lazy('myapp2:staff_list')
