from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
 
# 一般ユーザーおよびスーパーユーザーを作成するクラス
class CustomUserManager(BaseUserManager):
	# 一般ユーザーを作る時の処理内容を記述するメソッド
    def create_user(self, username, email, password=None):
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            password=password
        )
 
        user.set_password(password)
        user.save(using=self._db) # 操作している対象のオブジェクトの内容で、データベースを更新する
        return user

	# 管理権限のあるユーザーを作る時の処理内容を記述するメソッド 
    def create_superuser(self, username, email, password):
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        
        # 管理サイトで利用できるように、is_staff と is_superuser のフィールドも
        # true にしておく
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
 
 
# カスタムユーザーモデルを指定するクラス
class CustomUser(AbstractBaseUser):
    username = models.CharField('ユーザー名', max_length=100,
          unique=True,
          error_messages={
              'unique': ("同一のユーザー名が既に登録されています"),
           }, )
    email = models.EmailField('メールアドレス', unique=True,)
    age = models.PositiveIntegerField('年齢', default=0)
    is_admin = models.BooleanField('管理者', default=False)
    is_active = models.BooleanField('有効', default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    # メールアドレス(連絡先)として利用するフィールドを指定しておく
    EMAIL_FIELD = 'email'
    
    # ログイン時のユーザー名として使うフィールドを指定しておく
    USERNAME_FIELD = 'username'
 
	# createsuperuser コマンドを実行したときに追加で入力させるフィールドを複数指定
    REQUIRED_FIELDS = ['email']
 
	# UserManagerのクラスを指定しておく→ここで指定されたクラスを使って、ユーザーのデータを作る
    objects = CustomUserManager()
 
    def __str__(self):
        return self.username
 
    def get_full_name(self):
        return self.username

