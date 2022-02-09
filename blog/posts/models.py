from tabnanny import verbose
from django.db import models

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, verbose_name='작성자')
    title = models.CharField(max_length=256, verbose_name='제목', blank=False)
    content = models.TextField(verbose_name='글내용')
    image = models.ImageField(blank=True, verbose_name='이미지')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='수정날짜')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'
        verbose_name = '글'
        verbose_name_plural = '글'


class Comment(models.Model):
    post = models.ForeignKey(
        'posts.Post', on_delete=models.CASCADE, verbose_name='글')
    user = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, verbose_name='작성자')
    content = models.TextField(verbose_name='댓글내용')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='수정날짜')

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'comment'
        verbose_name = '댓글'
        verbose_name_plural = '댓글'
