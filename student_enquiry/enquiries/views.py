from django.shortcuts import render, redirect
from .forms import EnquiryForm
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Enquiry

def home(request):
    return render(request, 'home.html')

def enquiry_view(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enquiry_success')
    else:
        form = EnquiryForm()

    return render(request, 'enquiries/enquiry_form.html', {'form': form})

def enquiry_success_view(request):
    return render(request, 'enquiries/enquiry_success.html')

# from django.shortcuts import render
# from .models import Enquiry
#
# def enquiry_list(request):
#     # Fetch all enquiries from the database
#     enquiries = Enquiry.objects.all().order_by('-date')  # Order by most recent
#     return render(request, 'enquiries/enquiry_list.html', {'enquiries': enquiries})


# def enquiry_list(request):
#     # Retrieve all enquiries and order them by date (most recent first)
#     enquiries = Enquiry.objects.all().order_by('-date')
#
#     # Add pagination with 10 enquiries per page
#     paginator = Paginator(enquiries, 10)  # 10 enquiries per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     return render(request, 'enquiries/enquiry_list.html', {'page_obj': page_obj})



def enquiry_list(request):
    # Get filter parameters
    course = request.GET.get('course')
    experience = request.GET.get('experience')

    # Build the query
    enquiries = Enquiry.objects.all()
    if course:
        enquiries = enquiries.filter(course=course)
    if experience:
        enquiries = enquiries.filter(experience=experience)

    # Paginate the results
    paginator = Paginator(enquiries, 10)  # Show 10 enquiries per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # return render(request, 'enquiry_list.html', {'page_obj': page_obj})
    return render(request, 'enquiries/enquiry_list.html', {'page_obj': page_obj})


from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm
from .models import StudentRegistration

def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')  # Redirect to a success page
    else:
        form = StudentRegistrationForm()

    return render(request, 'register/register_student.html', {'form': form})
def registration_success(request):
    return render(request, 'register/register_student.html')


from django.shortcuts import render, redirect
from .forms import TrainerForm
from .models import Trainer
def trainer_view(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainer_success')
    else:
        form = TrainerForm()

    return render(request, 'trainer/trainer_form.html', {'form': form})

def trainer_success_view(request):
    return render(request, 'trainer/trainer_success.html')

def trainer_list(request):
    # Get filter parameters
    course = request.GET.get('course')
    experience = request.GET.get('experience')

    # Build the query
    trainer = Trainer.objects.all()

    # Paginate the results
    paginator = Paginator(trainer, 10)  # Show 10 enquiries per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # return render(request, 'enquiry_list.html', {'page_obj': page_obj})
    return render(request, 'trainer/trainer_list.html', {'page_obj': page_obj})