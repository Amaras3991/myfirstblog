from django.db import models


class Post(models.Model):
    title = models.CharField('Title', max_length=100)
    text = models.TextField('Post text')
    author = models.CharField('Author', max_length=100)
    pub_date = models.DateTimeField('Date published')

    def __str__(self):
        return f'{self.title}, {self.author}'


class Comments(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    email = models.EmailField()
    name = models.CharField('Name', max_length=100)
    comment_text = models.CharField('Comment text', max_length=1000)

    def __str__(self):
        return f'{self.name}, {self.post}'
