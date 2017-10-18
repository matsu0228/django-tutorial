
from django import forms
import numpy as np
import datetime

MONTH = np.arange(1,13)
MONTH  = tuple([(str(x),datetime.datetime.strptime(str(x), "%m").strftime("%b")) for x in MONTH])

YEAR = np.arange(2010,2018)
YEAR = tuple([(x,x) for x in YEAR[::-1]])

class DateForm(forms.Form):

  def __init__(self, *args, **kwargs):
    super(DateForm, self).__init__(*args, **kwargs)
    self.fields['month'] = forms.ChoiceField(choices = MONTH)
    self.fields['month'].widget.attrs['class'] = "selectpicker show-tick form-control col-lg-3"
    self.fields['month'].widget.attrs['data-live-search']="true"
    self.fields['year'] = forms.ChoiceField(choices = YEAR)
    self.fields['year'].widget.attrs['class'] = "selectpicker show-tick form-control"
    self.fields['year'].widget.attrs['data-live-search']="true"
