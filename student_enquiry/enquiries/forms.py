# from django import forms
# from .models import Enquiry
#
# class EnquiryForm(forms.ModelForm):
#     class Meta:
#         model = Enquiry
#         fields = ['name', 'email', 'phone', 'message']
from django import forms
from .models import Enquiry


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'email', 'phone', 'message', 'experience', 'batch_type', 'course', 'institute_reference']
        widgets = {
            'experience': forms.RadioSelect(choices=[('fresher', 'Fresher'), ('experienced', 'Experienced')]),
            'batch_type': forms.RadioSelect(choices=[('weekday', 'Weekday'), ('weekend', 'Weekend')]),
            'course': forms.Select(choices=Enquiry.COURSE_CHOICES),
            'institute_reference': forms.Select(choices=Enquiry.REFERENCE_CHOICES),
        }
from django import forms
from .models import StudentRegistration

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = '__all__'
        widgets = {
            'date_of_joining': forms.DateInput(attrs={'type': 'date'}),
        }

from django import forms
from .models import Trainer
class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'email', 'phone', 'occupation', 'experience', 'batch_type', 'course', 'branch_location', 'training_mode']
        widgets = {
            'batch_type': forms.RadioSelect(choices=[('weekday', 'Weekday'), ('weekend', 'Weekend')]),
            'course': forms.SelectMultiple(choices=Trainer.COURSE_CHOICES),
            'branch_location': forms.Select(choices=Trainer.LOCATION_CHOICES),
            'training_mode': forms.Select(choices=Trainer.MODE_CHOICES),
        }