from django.shortcuts import render, HttpResponse
from services.models import *
from monit.models import *
import datetime
import pprint
from django.utils import timezone

def Value_To_Hex_String(sString):
	if(len(sString) < 4):
		if(len(sString) == 3):
			sString = "0" + sString
		if(len(sString) == 2):
			sString = "00" + sString
		if(len(sString) == 1):
			sString = "000" + sString
	return sString

def Store_Packet_Monit(sPingPacket):
	#print(sPingPacket)
	sError = "None"
	if(sPingPacket[0] == '*' and sPingPacket[-1] == '!'):
		#print("Correct packet")
		sPingPacket = sPingPacket[1:]
		sPingPacket = sPingPacket[:-1]
		#print(sPingPacket)

		#skipping first packet 
		sPingPacket = sPingPacket[sPingPacket.index(',') + 1:]
		#print(sPingPacket)

		#skipping second packet
		sPingPacket = sPingPacket[sPingPacket.index(',') + 1:]
		#print(sPingPacket)

		# Get packet id and number of sensor followed by
		sCode = sPingPacket[:sPingPacket.index(',')]
		#print(sCode)
		sPingPacket = sPingPacket[sPingPacket.index(',') + 1:]
		#print(sPingPacket)
		
		#Get Temperature
		sTemp = sPingPacket[:sPingPacket.index(',')]
		#print(sTemp)
		ui16Temp = int(sTemp,16)
		sPingPacket = sPingPacket[sPingPacket.index(',') + 1:]
		#print(sPingPacket)

		#Get Humidity
		sHumid = sPingPacket[:sPingPacket.index(',')]
		#print(sHumid)
		ui16Humid = int(sHumid,16)
		sPingPacket = sPingPacket[sPingPacket.index(',') + 1:]
		#print(sPingPacket)

		#Get Heartbeat
		sHeartb = sPingPacket[:sPingPacket.index(',')]
		#print(sHeartb)
		ui16Heartb = int(sHeartb,16)
		sPingPacket = sPingPacket[sPingPacket.index(',') + 1:]
		#print(sPingPacket)

		#Get Buzzer Status
		sBuzState = sPingPacket[:sPingPacket.index(',')]
		#print(sBuzState)
		ui16BuzState = int(sBuzState,16)
		sPingPacket = sPingPacket[sPingPacket.index(',') + 1:]
		#print(sPingPacket)

		sTimeNow = timezone.now()
		sDObject = LogDataMonit(dbLogTime = sTimeNow, dbTemp = ui16Temp, dbHumid = ui16Humid,dbHeartb=ui16Heartb,dbBuzState=ui16BuzState)
		sDObject.save()
		return 1
	else:
		print("Invalid packet")
		return 0

def Response_Packet():
	sData = LogUserDataMonit.objects.latest("id")
	sString = "*000103,010400012C03000000,0104,"
	
	sTempT  = str(format(sData.dbTempLimit,'x'))
	sTempT = Value_To_Hex_String(sTempT)
	#print(sTempT)

	sHumidT  = str(format(sData.dbHumidLimit,'x'))
	sHumidT = Value_To_Hex_String(sHumidT)
	#print(sHumidT)

	sHeartTMin  = str(format(sData.dbHeartbLimitMin,'x'))
	sHeartTMin = Value_To_Hex_String(sHeartTMin)
	#print(sHeartTMin)

	sHeartTMax  = str(format(sData.dbHeartbLimitMax,'x'))
	sHeartTMax = Value_To_Hex_String(sHeartTMax)
	#print(sHeartTMax)


	sString = sString + sTempT + ',' + sHumidT + ',' + sHeartTMin + ',' + sHeartTMax + ',0!'
	return sString

def Ping_Packet(request):
	sPingPacket = request.GET.get('pkt','')
	sString = "*000000,000000000000000000,0000!"
	try:
		sDBObjects = Ping(dbPacket=sPingPacket)
		sDBObjects.save()
		ui8Response = Store_Packet_Monit(sPingPacket)
		sString = Response_Packet()

	except Exception as e:
		print("Ping Error " + str(e))
		sErrorLog = ErrorLog(dbError=e, dbErrorCode = "ErrorCode")

	return HttpResponse(sString)

