from django.db import models
from django.forms import widgets

PUNCH_CHOICES = (
    ('ClockedIn','CLOCKED_IN'),
    ('ClockedOut', 'CLOCKED_OUT')
)

class TimeEntry(models.Model):
    entry_date = models.DateField()
    punch = models.CharField(max_length=10, choices=PUNCH_CHOICES)
    time_punched = models.TimeField()
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Time Entry {self.entry_date}"
    
    class Meta:
        verbose_name_plural = "Time Entries"