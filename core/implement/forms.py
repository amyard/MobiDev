from django import forms

import validators
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from core.implement.models import UrlModel



class UrlForm(forms.ModelForm):

    full_url = forms.URLField(label='', max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your URL'}))
    short_url = forms.CharField(label='', required=False, max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your short URL (optional)'}))

    class Meta:
        model = UrlModel
        fields = ['full_url', 'short_url']


    def __init__(self, *args, **kwargs):
        super(UrlForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('full_url', css_class='form-group col-md-6 mb-0 ml-3'),
                Column('short_url', css_class='form-group col-md-4 mb-0 ml-3'),
                Column(Submit('submit', 'Create URL', css_class='btn btn-primary px-2 ml-3'),
                        css_class='form-group col-md-1 mb-0 ml-3'
                    ),
                css_class='form-row py-2'
            )
        )


    def clean_full_url(self):
        full_url = self.cleaned_data.get('full_url')
        if not validators.url(full_url):
            return forms.ValidationError('Incorrect url')
        if UrlModel.objects.filter(full_url=full_url).exists():
            self.add_error('full_url', 'Such url already exists in our DB.')
        return full_url

    def clean_short_url(self):
        short_url = self.cleaned_data.get('short_url')
        if short_url and UrlModel.objects.filter(short_url=short_url).exists():
            self.add_error('short_url', 'Short URL must be unique.')
        return short_url

