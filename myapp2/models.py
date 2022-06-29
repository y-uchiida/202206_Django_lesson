from django.db import models

# Create your models here.
 
# 従業員一人についての詳細データ
class StaffInformation(models.Model):
    staff_name = models.CharField('名前', max_length=100)
    email = models.EmailField('メールアドレス', blank=True, null=True)
    address = models.CharField('住所', blank=True, null=True, max_length=100)
    birthday = models.DateTimeField('誕生日', blank=True, null=True)
    hire_date = models.DateField('入社日', blank=True, null=True)
    at_desk = models.BooleanField('出社状態', default=False)
 
    def __str__(self):
        return self.staff_name

# 部署の一覧テーブル
# staff_informationの側で、foreign keyを持っている
# class Department(models.Model):
#     name = models.CharField('部署名', unique=True, max_length=100)
#     def __str__(self):
#         return self.name

# 従業員のデータ
class Staff(models.Model):
    name = models.CharField('ビジネスネーム', max_length=100)
    information = models.OneToOneField(StaffInformation, on_delete=models.CASCADE, verbose_name=("社員情報"), null=True)
    # department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name=("所属部署"), null=True)
 
    def __str__(self):
        return self.name


