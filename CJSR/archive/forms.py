from django import forms
from archive.fields import JqSplitDateTimeField
from archive.widgets import JqSplitDateTimeWidget
class TimeLookupForm(forms.Form):
    date_time = JqSplitDateTimeField(widget=JqSplitDateTimeWidget(attrs={'date_class':'datepicker','time_class':'timepicker'}))
