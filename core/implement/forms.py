from django import forms
from core.implement.models import UrlModel
import validators


class UrlForm(forms.ModelForm):

    full_url = forms.URLField(label='', max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your URL'}))
    short_url = forms.URLField(label='', max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your short URL (optional)'}))

    class Meta:
        model = UrlModel
        fields = ['full_url', 'short_url']


    def clean_full_url(self):
        full_url = self.cleaned_data.get('full_url')
        if not validators.url(full_url):
            return self.ValidationError('Incorrect url')
        return full_url

    def clean_short_url(self):
        short_url = self.cleaned_data.get('short_url')
        if short_url and UrlModel.objects.filter(short_url=short_url).exists():
            return self.ValidationError('Url must be unique')
        return short_url


