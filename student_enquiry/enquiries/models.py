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


class Option(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'courses_master'

class Trainer(models.Model):
    BATCH_TYPE_CHOICES = [
        ('all', 'All'),
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
        ('virtual', 'Virtual'),
        ('btm', 'BTM'),
        ('marathahalli', 'Marathahalli'),
        ('kalyannagar', 'Kalyan Nagar'),

    ]

    MODE_CHOICES = [
        ('hybrid', 'Hybrid'),
        ('online', 'Online'),
        ('offline', 'Offline'),

    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=500)
    occupation = models.CharField(max_length=250)
    experience = models.CharField(max_length=250)

    batch_type = models.CharField(max_length=10, choices=BATCH_TYPE_CHOICES, default='all')
    #course = MultiSelectField(choices=COURSE_CHOICES)
    #course = models.CharField(max_length=100, choices=COURSE_CHOICES, default='select')
    course = models.ManyToManyField(Option)
    branch_location = models.CharField(max_length=100, choices=LOCATION_CHOICES, default='virtual')
    training_mode = models.CharField(max_length=100, choices=MODE_CHOICES, default='hybrid')
    date_of_joining = models.DateField()
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'trainer_details'

    def __str__(self):
        return self.name
    # def __str__(self):
    #     return ', '.join(str(option) for option in self.course.all())



class StudentRegistration(models.Model):
    PAYMENT_MODES = [
        ('Credit Card', 'Credit Card'),
        ('Debit Card', 'Debit Card'),
        ('Cash', 'Cash'),
        ('Bank Transfer', 'Bank Transfer'),
    ]

    BATCH_TYPES = [
        ('all', 'All'),
        ('Weekday', 'Weekday'),
        ('Weekend', 'Weekend'),
    ]

    #registration_number = models.CharField(max_length=20, unique=True)
    date_of_joining = models.DateField()
    student_name = models.CharField(max_length=100)
    student_mobile = models.CharField(max_length=15)
    student_email = models.CharField(max_length=250)
    student_address = models.CharField(max_length=500)
    #student_pincode = models.CharField(max_length=10)
    student_pincode = models.IntegerField()
    course_name = models.CharField(max_length=100)
    total_fees = models.DecimalField(max_digits=10, decimal_places=2)
    fee_paid = models.DecimalField(max_digits=10, decimal_places=2)
    fee_remaining = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    payment_mode = models.CharField(max_length=20, choices=PAYMENT_MODES, default='Cash')
    last_date_to_pay = models.DateField(null=True)
    #trainer_name = models.CharField(max_length=100)
    #trainer_name = models.ManyToManyField(Trainer)
    trainer_name = models.ForeignKey(Trainer,on_delete=models.SET_NULL, null=True)
    batch_type = models.CharField(max_length=10, choices=BATCH_TYPES, default='all')
    remarks = models.TextField(null=True)

    class Meta:
        db_table = 'student_details'

class Receipt(models.Model):
    number = models.PositiveIntegerField()  # The receipt number
    year = models.PositiveIntegerField()     # The year for the receipt

    def __str__(self):
        return f"{self.number}-{self.year}"  # Format like 1-YYYY

class PaymentDetails(models.Model):
    student_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_mode = models.CharField(max_length=20)
    payment_date = models.DateField()
    receipt_no = models.CharField(max_length=20)


    class Meta:
        db_table = 'payment_details'