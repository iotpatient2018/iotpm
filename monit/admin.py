from django.contrib import admin
from monit.models import LogDataMonit,LogUserDataMonit,LogErrorMonit


admin.site.register(LogDataMonit)
admin.site.register(LogUserDataMonit)
admin.site.register(LogErrorMonit)
