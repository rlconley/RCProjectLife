from django import forms
# from .models import Contact, Note

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'name',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'phone_number',
            'email',
            'birthday',
        ]
        widgets = {'birthday': forms.SelectDateWidget()
        }