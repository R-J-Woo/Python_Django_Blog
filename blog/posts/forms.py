from django import forms
from .models import Post


class WriteForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required': '제목을 입력해주세요'
        }, max_length=64, label='제목'
    )
    content = forms.CharField(
        error_messages={
            'required': '본문을 입력해주세요'
        }, max_length=64, label='본문'
    )
    image = forms.ImageField(label='이미지')

    def claen(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        image = cleaned_data.get('image')

        if title and content:
            post = Post(
                title=title,
                content=content,
                image=image
            )
            post.save()
