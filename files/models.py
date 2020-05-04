from django.db import models

class File(models.Model):
    file = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.file.name

class Image(models.Model):
    file = models.ImageField(blank=False, null=False)
    def __str__(self):
        return self.file.name


class TestModel(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)