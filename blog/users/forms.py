from django import forms
from .models import User
from django.contrib.auth.hashers import check_password, make_password


class RegisterForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': '사용자명을 입력해주세요'
        }, max_length=64, label='사용자명'
    )
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요'
        }, max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요'
        }, widget=forms.PasswordInput, label='비밀번호'
    )
    re_password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요'
        }, widget=forms.PasswordInput, label='비밀번호 확인'
    )

    def clean(self):  # 유효성 검사하는 함수
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error('password', '비밀번호가 서로 다릅니다.')
                self.add_error('re_password', '비밀번호가 서로 다릅니다.')
            else:
                user = User(
                    username=username,
                    email=email,
                    password=make_password(password)
                )
                user.save()


class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요'
        }, max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요'
        }, widget=forms.PasswordInput, label='비밀번호'
    )

    def clean(self):  # 유효성 검사하는 함수
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                self.add_error('email', '이메일이 존재하지 않습니다.')
                return

            if not check_password(password, user.password):
                self.add_error('password', '비밀번호를 틀렸습니다.')
            else:
                self.user_id = user.id
