from django.db import models

# Create your models here.
class Customer(models.Model):
	cid=models.AutoField(primary_key=True)
	name=models.CharField(max_length=10)
	sex=models.IntegerField(default=0)
	phone=models.IntegerField(default=0)
	age=models.IntegerField(default=0)
	job=models.TextField(default='未知')
	money=models.IntegerField(default=0)
	hobby=models.TextField(default='未知')
	house=models.IntegerField(default='未知')
	contact=models.TextField(default='尽快开始接触哦')
