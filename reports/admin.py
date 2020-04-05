from django.contrib import admin
from reports.models import Report

from django.shortcuts import render
from django.contrib.admin import AdminSite

from django.urls import path

class MyAdminSite(AdminSite):
    def get_urls(self):
        from django.conf.urls import url
        urls = super(MyAdminSite, self).get_urls()
        # Note that custom urls get pushed to the list (not appended)
        # This doesn't work with urls += ...
        urls = [
            url(r'^reloaddata/$', reloaddata)
        ] + urls
        return urls

admin_site = MyAdminSite()

def reloadDataForm(modeladmin, request, queryset):
    return render(request, 'admin/reloaddata_intermediate.html', context={})

class ReportAdmin(admin.ModelAdmin):
    list_display = ['ca', 'date', 'cases', 'deceases', 'cured', 'hospitalized', 'uci', 'accIncidence', 'diffCases']
    ordering = ['ca', 'date']
    actions = [reloadDataForm]

admin_site.register(Report, ReportAdmin)


from django.contrib.admin.views.decorators import staff_member_required
@staff_member_required
def reloaddata(request):
    from django.core.management import call_command
    from django.http import HttpResponseRedirect

    breakpoint()

    url = request.POST['csv_url']
    call_command('reloaddata', url)
    return HttpResponseRedirect("/admin/reports")
