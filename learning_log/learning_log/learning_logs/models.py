from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    text = models.CharField(max_length=100)
    date_add = models.DateTimeField('Published date', auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Record(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'records'

    def __str__(self):
        if len(self.text) < 50:
            return self.text
        return f'{self.text[:50]}...'

