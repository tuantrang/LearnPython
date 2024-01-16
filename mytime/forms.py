from django.forms import ModelForm
from .models import TimeEntry

class TimeEntryForm(ModelForm):
    class Meta:
        model= TimeEntry
        fields = '__all__'