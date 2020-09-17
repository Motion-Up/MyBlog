from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=300)
    date = models.DateTimeField(null=True)
    text = models.TextField()
    image = models.ImageField(upload_to='event_images/')

    def get_summary(self):
        '''Возвращает не весь текст а только его часть'''
        return self.text[:30] + '...'

    def __str__(self):
        '''Функция для отображения в админке заголовков'''
        return self.title

