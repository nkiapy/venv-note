from django.db import models

# Create your models here.
# 테이블을 정의하는 파일

class Test(models.Model):
    sample_text = models.CharField(max_length=200)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Memo(models.Model):
    username = models.CharField(max_length=150)
    title = models.CharField(max_length=100)  # 길이 제한이 있는 문자열
    content = models.TextField(verbose_name='내용')  # 길이 제한이 없는 문자열
    tags = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)  # 해당 레코드 생성시 현재 시간 자동저장
    updated_date = models.DateTimeField(auto_now=True)  # 해당 레코드 갱신시 현재 시간 자동저장