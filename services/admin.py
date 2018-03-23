from django.contrib import admin
from services.models import Ping,ErrorLog

admin.site.register(Ping)
admin.site.register(ErrorLog)
