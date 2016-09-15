__author__ = 'krishnasagar'

from django import forms
from django.core.exceptions import ValidationError

# Refer for forms.MultipleChoiceField always, its helpful - http://www.programcreek.com/python/example/58199/django.forms.MultipleChoiceField

class TrackForm(forms.Form):
    def __init__(self, *args, **kwargs):
        if 'choices' in kwargs:
            choices = kwargs.pop('choices')
        else:
            choices = None
        super(TrackForm, self).__init__( *args, **kwargs)
        self.fields['tname'] = forms.CharField(label='Track Name', max_length=100,
                            widget=forms.TextInput(attrs={'title':'Track name upto 100 characters'}))
        self.fields['rating'] = forms.DecimalField(label='Rating', max_value=10.0,
                                min_value=0.0, decimal_places=1, max_digits=2, required=False)#.widget_attrs({'title':'Rating from 0 to 10'})
        if choices != None:
            self.fields['gname'] = forms.MultipleChoiceField(label="Genre Names", widget=forms.SelectMultiple(attrs={'title': 'Multiple Select using RCtrl+Mouse Left Key'}),
                                                             required=False, choices = choices)
        else:
            self.fields['gname'] = forms.MultipleChoiceField(label="Genre Names", widget=forms.SelectMultiple(attrs={'title': 'Multiple Select using RCtrl+Mouse Left Key'}),
                                      required=False)#, choices = ((1,'    '),(2,'    '), ))
        #gname = CharField(label='Genre Name', required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter genre(s) seperated by commas'}))
        #((4, 'bollywood'), (5, 'melody'), (6, 'rock'), (8, 'hippie hop'), (13, 'kushwaha'), (14, 'New Gen'), (15, 'snooze'), (30, 'hollywood 2'), (31, 'hollywood2'), (32, 'bollywood'))

    '''def clean(self):
        cleaned_data = super(TrackForm, self).clean()
        if cleaned_data.get('tname') == None:
            self.add_error('tname','Music Track Name required!!!!')
        else:
            return cleaned_data'''

class GenreForm(forms.Form):
    gname = forms.CharField(label='Genre Name', max_length=100,
                            widget=forms.TextInput(attrs={'title':'Genre name upto 100 characters', 'placeholder' : 'Required'}))