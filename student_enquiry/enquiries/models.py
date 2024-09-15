from django.db import models
#
#
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
        ('python', 'Python'),
        ('java', 'Java'),
        ('data_science', 'Data Science'),
    ]

    REFERENCE_CHOICES = [
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
    course = models.CharField(max_length=20, choices=COURSE_CHOICES, default='python')
    institute_reference = models.CharField(max_length=20, choices=REFERENCE_CHOICES, default='online')
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
