from django import forms 
from app1_shortner.models import tbl_URL_Shortner

class URL_Shortner_Form(forms.ModelForm):
    class Meta:
        model = tbl_URL_Shortner
        fields = ['long_url'] 

