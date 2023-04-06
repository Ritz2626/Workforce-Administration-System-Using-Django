from django import forms

class UploadFileForm(forms.Form):
    name1=forms.CharField()
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
   