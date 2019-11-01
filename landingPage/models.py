from django.db import models
from django.utils import timezone
# Create your models here.

class StatusModels(models.Model):
	status = models.CharField(max_length=300)
	post_time = models.DateTimeField(default=timezone.now)