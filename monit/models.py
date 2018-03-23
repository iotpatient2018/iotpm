from django.db import models
from django.utils import timezone

class LogDataMonit(models.Model):
	dbLogTime  = models.DateTimeField(auto_now_add=True)
	dbTemp     = models.IntegerField(default=0)
	dbHumid    = models.IntegerField(default=0)
	dbHeartb   = models.IntegerField(default=0)
	dbBuzState = models.IntegerField(default=0)

	def __str__(self):
		return str(self.dbHeartb)

class LogUserDataMonit(models.Model):
	dbLogTime        = models.DateTimeField(auto_now_add=True)
	dbTempLimit      = models.IntegerField(default=0)
	dbHumidLimit     = models.IntegerField(default=0)
	dbHeartbLimitMin = models.IntegerField(default=0)
	dbHeartbLimitMax = models.IntegerField(default=0)
	
	def __str__(self):
		return str(self.dbHeartbLimitMin)

class LogErrorMonit(models.Model):
	dbErrorMonit     = models.CharField(max_length=500)
	dbErrorTimeMonit = models.DateTimeField(auto_now_add=True)
	dbErrorCodeMonit = models.CharField(max_length = 500)

	def  __str__(self):
		return str(self.dbErrorMonit)