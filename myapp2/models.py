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
class Department(models.Model):
    name = models.CharField('部署名', unique=True, max_length=100)
    def __str__(self):
        return self.name

# 会社の所有書籍のデータ
class Book(models.Model):
    name = models.CharField('書籍名', max_length=100)
    management_code = models.CharField('管理番号', unique=True, max_length=50)
 
    def __str__(self):
        return self.name

# 従業員のデータ
class Staff(models.Model):
    name = models.CharField('ビジネスネーム', max_length=100)
    information = models.OneToOneField(StaffInformation, on_delete=models.CASCADE, verbose_name=("社員情報"), null=True)
    
    # 部署のテーブルとの関連付けを表現するリレーションの設定
    # Staffからみると、所属する部署はひとつだけなので、多対一の関連になる
    # ForeignKey(連携先のモデル名, on_delete=削除されたときの動作)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name=("所属部署"), null=True)
 
    # 会社の書籍のテーブルとの可憐付けを表現するリレーション
    # 履歴として考えたとき、一冊の本が過去に他の社員さんに借りられている場合があるので、多対多の関連になる
    # MenyToManyFileld(<連携先モデル名>)
    rented_books = models.ManyToManyField(Book, verbose_name=("借りている本"))
 
    def __str__(self):
        return self.name
