from django.db import models
class Enquiry(models.Model):
    FRESHER_OR_EXPERIENCED = [
        ('fresher', 'Fresher'),
        ('experienced', 'Experienced'),
    ]

    BATCH_TYPE_CHOICES = [
        ('weekday', 'Weekday'),
        ('weekend', 'Weekend'),
    ]


    COURSE_CHOICES = [
        ('select', 'Select'),
        ('python', 'Python'),
        ('java', 'Java'),
        ('data_science', 'Data Science'),
    ]
    REFERENCE_CHOICES = [
        ('select', 'Select'),
        ('online', 'Online Advertisement'),
        ('friend', 'Friend Referral'),
        ('social_media', 'Social Media'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    # Update max_length to 11
    experience = models.CharField(max_length=11, choices=FRESHER_OR_EXPERIENCED, default='fresher')

    batch_type = models.CharField(max_length=10, choices=BATCH_TYPE_CHOICES, default='weekday')
    course = models.CharField(max_length=20, choices=COURSE_CHOICES, default='select')
    institute_reference = models.CharField(max_length=20, choices=REFERENCE_CHOICES, default='select')
    date = models.DateTimeField(auto_now_add=True)
#
#
# from django.db import models
#
#
# class StudentRegistration(models.Model):
#     PAYMENT_MODES = [
#         ('Credit Card', 'Credit Card'),
#         ('Debit Card', 'Debit Card'),
#         ('Cash', 'Cash'),
#         ('Bank Transfer', 'Bank Transfer'),
#     ]
#
#     BATCH_TYPES = [
#         ('Weekday', 'Weekday'),
#         ('Weekend', 'Weekend'),
#     ]
#
#     registration_number = models.CharField(max_length=20, unique=True)
#     date_of_joining = models.DateField()
#     student_name = models.CharField(max_length=100)
#     course_name = models.CharField(max_length=100)
#     total_fees = models.DecimalField(max_digits=10, decimal_places=2)
#     remaining_fees = models.DecimalField(max_digits=10, decimal_places=2)
#     payment_mode = models.CharField(max_length=20, choices=PAYMENT_MODES)
#     trainer_name = models.CharField(max_length=100)
#     batch_type = models.CharField(max_length=10, choices=BATCH_TYPES)
#     remarks = models.TextField(blank=True)
#
#     def __str__(self):
#         return self.registration_number
from django.db import models
# class Enquiry(models.Model):
#     EXPERIENCE_CHOICES = [
#         ('Fresher', 'Fresher'),
#         ('Experienced', 'Experienced'),
#     ]
#
#     BATCH_CHOICES = [
#         ('Weekday', 'Weekday'),
#         ('Weekend', 'Weekend'),
#     ]
#
#     COURSE_CHOICES = [
#         ('Python', 'Python'),
#         ('Java', 'Java'),
#         ('Data Science', 'Data Science'),
#     ]
#
#     INSTITUTE_REFERENCE_CHOICES = [
#         ('Internet', 'Internet'),
#         ('Referral', 'Referral'),
#         ('Advertisement', 'Advertisement'),
#         ('Other', 'Other'),
#     ]
#
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.CharField(max_length=15)
#     experience = models.CharField(max_length=11, choices=EXPERIENCE_CHOICES)
#     batch_type = models.CharField(max_length=10, choices=BATCH_CHOICES)
#     course = models.CharField(max_length=20, choices=COURSE_CHOICES)
#     institute_reference = models.CharField(max_length=20, choices=INSTITUTE_REFERENCE_CHOICES)
#     date = models.DateField()
#
#     def __str__(self):
#         return self.name


class StudentRegistration(models.Model):
    PAYMENT_MODES = [
        ('Credit Card', 'Credit Card'),
        ('Debit Card', 'Debit Card'),
        ('Cash', 'Cash'),
        ('Bank Transfer', 'Bank Transfer'),
    ]

    BATCH_TYPES = [
        ('Weekday', 'Weekday'),
        ('Weekend', 'Weekend'),
    ]

    registration_number = models.CharField(max_length=20, unique=True)
    date_of_joining = models.DateField()
    student_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    total_fees = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_fees = models.DecimalField(max_digits=10, decimal_places=2)
    payment_mode = models.CharField(max_length=20, choices=PAYMENT_MODES)
    trainer_name = models.CharField(max_length=100)
    batch_type = models.CharField(max_length=10, choices=BATCH_TYPES)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.registration_number

from multiselectfield import MultiSelectField
class Trainer(models.Model):
    BATCH_TYPE_CHOICES = [
        ('weekday', 'Weekday'),
        ('weekend', 'Weekend'),
    ]

    COURSE_CHOICES = [
        ('select', 'Select'),
        ('python', 'Python'),
        ('java', 'Java'),
        ('data_science', 'Data Science'),
        ('dba', 'Database Administrator'),
        ('php', 'PHP'),
    ]

    LOCATION_CHOICES = [
        ('select', 'Select'),
        ('btm', 'BTM'),
        ('marathahalli', 'Marathahalli'),
        ('kalyannagar', 'Kalyan Nagar'),
    ]

    MODE_CHOICES = [
        ('select', 'Select'),
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    occupation = models.CharField(max_length=250)
    experience = models.CharField(max_length=250)

    batch_type = models.CharField(max_length=10, choices=BATCH_TYPE_CHOICES, default='weekday')
    course = MultiSelectField(choices=COURSE_CHOICES)
    branch_location = models.CharField(max_length=100, choices=LOCATION_CHOICES, default='select')
    training_mode = models.CharField(max_length=100, choices=MODE_CHOICES, default='select')
    date = models.DateTimeField(auto_now_add=True)