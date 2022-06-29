from django.db import models
 
class Comment(models.Model):
    title = models.CharField('タイトル', max_length=100, )
    author = models.CharField('投稿者', max_length=100, )
    text = models.TextField('投稿内容')
    date = models.DateField('投稿日時', auto_now_add=True, )
 
    def __str__(self):
        return self.title
