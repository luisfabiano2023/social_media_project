from django.db import models




from django.db import models

class User(models.Model):
	username = models.CharField(max_length=255)
	name=models.CharField(max_length=255)    
	email=models.EmailField(max_length=255)
	def __str__(self) -> str:
		return self.name


