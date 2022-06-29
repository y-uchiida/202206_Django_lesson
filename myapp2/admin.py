from django.contrib import admin

from .models import Staff
from .models import StaffInformation
from .models import Department
from .models import Book

# Register your models here.

# 管理画面に表示するクラスを登録する
admin.site.register(Staff)
admin.site.register(StaffInformation)
admin.site.register(Department)
admin.site.register(Book)
