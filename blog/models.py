from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(max_length=290, verbose_name='Описание')
    content = models.TextField(verbose_name='Содержание')
    image = models.ImageField(upload_to='news_pics', verbose_name='Изображение', blank=True)
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def number_of_comments(self):
        return Comment.objects.filter(post_connected=self).count()

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-date', ]
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    post_connected = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Содержание')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.author) + ', ' + self.post_connected.title[:40]
