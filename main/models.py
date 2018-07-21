from django.db import models

from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=200, default  = "sada")
    long_text = models.TextField(max_length=200, default = '')
class Choice(models.Model):
    DoesNotExist = None
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
