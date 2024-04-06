from django.contrib import admin

from .models import Member

from .models import Employee

# Register your models here.
admin.site.register(Member),
admin.site.register(Employee)