from django.shortcuts import render, HttpResponse
from monit.models import *
import pprint
import json

def Display_All(request):
	if(request.POST):
		if request.is_ajax():
			code = request.POST['code']
			hmax = request.POST['hmax']
			hmin = request.POST['hmin']
			tem  = request.POST['tem']
			hum  = request.POST['hum']
			
			ui8Process = 0
			#print(code)
			sSet = LogUserDataMonit.objects.latest("id")
			if(int(code) == 1):
				if hmax:
					if hmax.isalpha() == False:
						sSet.dbHeartbLimitMax = int(hmax)
						ui8Process = 1

			if(int(code) == 2):
				if hmin:
					if hmin.isalpha() == False:
						sSet.dbHeartbLimitMin = int(hmin)
						ui8Process = 1

			if(int(code) == 3):
				if tem:
					if tem.isalpha() == False:
						sSet.dbTempLimit = int(tem)
						ui8Process = 1
				
			if(int(code) == 4):
				if hum:
					if hum.isalpha() == False:
						sSet.dbHumidLimit = int(hum)
						ui8Process = 1
			
			if(ui8Process == 1):
				try:
					sTimeNow = timezone.now()
					sDObject = LogUserDataMonit(dbLogTime = sTimeNow, dbTempLimit = sSet.dbTempLimit, dbHumidLimit = sSet.dbHumidLimit,
						dbHeartbLimitMin=sSet.dbHeartbLimitMin,dbHeartbLimitMax=sSet.dbHeartbLimitMax)
					sDObject.save()
					msg = "New reset value added"
					return HttpResponse(json.dumps({'msg':msg}), content_type="application/json")	
				except Exception as e:
					msg = "Error in add "
					return HttpResponse(json.dumps({'msg':msg}), content_type="application/json")
			else:
				msg = "Error in sending data only number allowed"
				return HttpResponse(json.dumps({'msg':msg}), content_type="application/json")
	else:
		try:
			sLog = LogDataMonit.objects.latest("id")
			#print('sLog')
			#print(sLog)
			sSet  = LogUserDataMonit.objects.latest("id")
			#print('sSet')
			#print(sSet)
			sData = {'Log':sLog,'Set':sSet}
			#print('sData')
		except Exception as e:
			sData = 'Data'
			print(e)
		return render(request, 'monit/index.html',{'Data':sData})