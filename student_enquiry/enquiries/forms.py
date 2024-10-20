from django import forms
from .models import Enquiry
from .models import StudentRegistration
from .models import Trainer


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

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        #fields = '__all__'
        fields = ['student_name','student_mobile','student_email','student_address','student_pincode','course_name','date_of_joining','total_fees','fee_paid','fee_remaining','payment_mode','last_date_to_pay','trainer_name','batch_type','remarks']
        widgets = {
            'date_of_joining': forms.DateInput(attrs={'type': 'date'}),
            'payment_mode': forms.Select(choices=StudentRegistration.PAYMENT_MODES),
            'batch_type': forms.Select(choices=StudentRegistration.BATCH_TYPES),
            'last_date_to_pay': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(StudentRegistrationForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['fee_remaining'].required = False
        self.fields['last_date_to_pay'].required = False
        self.fields['remarks'].required = False


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'email', 'phone', 'address', 'occupation', 'experience', 'batch_type', 'course','date_of_joining', 'branch_location', 'training_mode']
        widgets = {
            'date_of_joining': forms.DateInput(attrs={'type': 'date'}),
            'batch_type': forms.Select(choices=[('weekday', 'Weekday'), ('weekend', 'Weekend')]),
            'course': forms.CheckboxSelectMultiple(),
            'branch_location': forms.Select(choices=Trainer.LOCATION_CHOICES),
            'training_mode': forms.Select(choices=Trainer.MODE_CHOICES),
        }