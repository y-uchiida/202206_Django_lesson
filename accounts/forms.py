from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import AuthenticationForm

# 自作のユーザーアカウントの作成のフォーム
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'is_active')


# 管理サイトへのログインの際などに発生するAttributeErrorを回避するため、
# confirm_login_allowed をオーバーライドするクラスを作成しておく
class LoginAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                ("アカウントが無効です"),
                code='inactive',
            )
        if not user.is_admin:
            raise forms.ValidationError(
                ("管理者権限を持っていません"),
                code='notadmin'
            )
