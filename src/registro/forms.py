from django import forms

from .models import Register

class PostRegister(forms.Form):

    name = forms.CharField(label="Nome completo", max_length=100)
    birthdate = forms.DateField(label="Data de nascimento")
    testtype = forms.CharField(max_length=100)
    testresult = forms.CharField(max_length=100)

    class Meta:
        model = Register
        fields = '__all__'
