from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    type = models.BooleanField('pytanie zamkniete', default=True)
    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    user_answer = models.CharField(default="Empty Answer", max_length=100)
    def __str__(self):
        return self.user_answer

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text