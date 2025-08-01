from django.contrib import admin
from home1.models import Job_information
from home1.models import Job_information1
from home1.models import addjobs
from home1.models import contactus
from home1.models import save_form

# Register your models here.
admin.site.register(Job_information)
admin.site.register(Job_information1)
admin.site.register(contactus)
admin.site.register(addjobs)
admin.site.register(save_form)


