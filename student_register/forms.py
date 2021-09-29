from django import forms
from .models import Student,Year


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('fullname','division','studentId','year')
        labels = {
            'fullname':'Full Name',
            'division':'Student Division'
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm,self).__init__(*args, **kwargs)
        self.fields['year'].empty_label = "Select"
        self.fields['division'].required = False
