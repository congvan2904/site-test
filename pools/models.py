from django.db import models

# Create your models here.
class Question(models.Model):
	"""docstring for ClassName"""
	question_test=models.CharField(max_length=200)
	time_pub=models.DateTimeField()
class Choice(models.Model):
	"""docstring for ClassName"""
	question=models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text=models.CharField(max_length=100)
	vote=models.IntegerField(default=0)
		
		