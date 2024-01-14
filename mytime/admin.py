from django.contrib import admin

from mytime.models import TimeEntry

admin.site.site_header = "My Time"

class TimeEntryAdmin(admin.ModelAdmin):
    list_display=['entry_date','punch', 'time_punched','note']

    class Meta:
        model: TimeEntry

admin.site.register(TimeEntry, TimeEntryAdmin)        