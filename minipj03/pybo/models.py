from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200)  # 최대 200자
    content = models.TextField()                # 글자수 제한 없음
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    # 답변과 연결된 질문이 삭제될 경우 답변도 함께 삭제
    content = models.TextField()
    create_date = models.DateTimeField()
