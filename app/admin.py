from django.contrib import admin

from app.models import Task, Tenant

admin.AdminSite.site_header = "Im freihoefl 17 admin page"


admin.site.register(Task)
admin.site.register(Tenant)