from django.contrib import admin
from first_app.models import AccessRecord,topic,Webpage
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(topic)
admin.site.register(Webpage)