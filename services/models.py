from django.db import models
from django.utils import timezone

class Ping(models.Model):
	dbPacket = models.CharField(max_length=500)
	dbTime   = models.DateTimeField(auto_now_add=True)

	def  __str__(self):
		return str(self.dbTime)


class ErrorLog(models.Model):
	dbError     = models.CharField(max_length=500)
	dbErrorTime = models.DateTimeField(auto_now_add=True)
	dbErrorCode = models.CharField(max_length = 500)

	def  __str__(self):
		return str(self.dbError)