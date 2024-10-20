from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import EnquiryForm
from django.core.paginator import Paginator
from .models import Enquiry
from django.db import connection
from .forms import StudentRegistrationForm
from .models import StudentRegistration
from .forms import TrainerForm
from .models import Trainer
from django.template import loader
from xhtml2pdf import pisa
from decimal import Decimal
from .utils import generate_receipt_number
from .models import PaymentDetails
from datetime import datetime



@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'dashboard/dashboard.html')

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


def register_student(request):
    # return render(request, 'register/student_success.html', {'idv': 9})
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            instance = form.save()
            My_new_id = instance.id
            return render(request, 'register/student_success.html',{'idv':My_new_id})
            #return redirect('registration_success')  # Redirect to a success page
    else:
        form = StudentRegistrationForm()

    return render(request, 'register/register_student.html', {'form': form})

def registration_success(request):
    return render(request, 'register/student_success.html')

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


# def trainer_list(request):
#     # Get filter parameters
#     #course = request.GET.get('course')
#     #experience = request.GET.get('experience')
#
#     # Build the query
#     trainer = Trainer.objects.prefetch_related('course').all()
#
#     # Paginate the results
#     paginator = Paginator(trainer, 10)  # Show 10 enquiries per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     # return render(request, 'enquiry_list.html', {'page_obj': page_obj})
#     return render(request, 'trainer/trainer_list.html', {'page_obj': page_obj})

def trainer_list(request):
    with connection.cursor() as cursor:
        cursor.execute("select a.id,a.name,a.email,a.phone,a.address,a.occupation,a.experience,a.batch_type,a.branch_location,a.training_mode,a.date_of_joining,a.date,to_char(date_of_joining,'dd-mm-yyyy') as dateofjoining,(select string_agg(name,', ') from trainer_details_course b,courses_master c where trainer_id=a.id and b.option_id=c.id) as courses from trainer_details a order by a.id")
        rows = cursor.fetchall()
    results = []
    for row in rows:
        results.append({
            'id': row[0],
            'name': row[1],
            'email': row[2],
            'phone': row[3],
            'address': row[4],
            'occupation': row[5],
            'experience': row[6],
            'batch_type': row[7],
            'branch_location': row[8],
            'training_mode': row[9],
            'courses': row[13],
            'date_of_joining': row[12],
        })
    return render(request, 'trainer/trainer_list.html', {'results': results})

def render_to_pdf(template_src, filename, context_dict={}):
    template = loader.get_template(template_src)
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="'+filename+'.pdf"'

    # Create a PDF from the HTML
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def calculate_components(total_amount, gst_rate):
    total_amount = Decimal(total_amount)
    gst_rate = Decimal(gst_rate)

    # Calculate Rate
    rate = total_amount / (1 + gst_rate)

    # Calculate CGST and SGST
    cgst = (gst_rate / Decimal(2)) * rate
    sgst = cgst  # Since CGST and SGST are equal

    return round(rate, 2), round(cgst, 2), round(sgst, 2)

def generate_receipt(request):
    if request.method == 'POST':
        st_id = request.POST.get('st_id')
        with connection.cursor() as cursor:
            query = "select a.id,a.student_name,a.student_email,a.student_mobile,a.student_address,a.course_name,a.fee_paid,a.payment_mode from student_details a where a.id=%s order by a.id"
            cursor.execute(query, [st_id])
            rows = cursor.fetchall()

        for row in rows:
            id = row[0]
            name = row[1]
            email = row[2]
            phone = row[3]
            address = row[4]
            course_name = row[5]
            fee_paid = row[6]
            payment_mode = row[7]
            # results.append({
            #     'id': row[0],
            #     'name': row[1],
            #     'email': row[2],
            #     'phone': row[3],
            #     'address': row[4],
            # })
        gst_rate = 0.18
        rate, cgst, sgst = calculate_components(fee_paid, gst_rate)

        receipt = generate_receipt_number()
        current_date = datetime.now().date()
        formatted_date = current_date.strftime('%Y-%m-%d')
        payment_det = PaymentDetails(
            student_id=id,
            amount=fee_paid,
            payment_mode=payment_mode,
            payment_date=formatted_date,
            receipt_no=receipt
        )
        payment_det.save()

        context = {
            'id': id,
            'name': name,
            'email': email,
            'mobile': phone,
            'address': address,
            'course_name': course_name,
            'fee_paid': fee_paid,
            'payment_mode': payment_mode,
            'rate': rate,
            'cgst': cgst,
            'sgst': sgst,
            'receipt': receipt,
            'paid_on': formatted_date
        }
        filename = 'Receipt_'+name
        return render_to_pdf('receipt.html',filename, context)
        #return render(request, 'receipt.html', context)
        #return HttpResponse(f"{id}")

def testReceipt(request):
    return render(request, 'receipt_test.html')
    #return render_to_pdf('receipt_test.html','report')

def reGenerateReceipt(request):
    if request.method == 'POST':
        receipt_no = request.POST.get('receipt_no')
        receipt_year = request.POST.get('receipt_year')
        qreceipt = receipt_no+"-"+receipt_year
        with connection.cursor() as cursor:
            query = "select a.amount,a.payment_mode,a.payment_date::text as payment_date,a.receipt_no,b.student_name,b.student_mobile,b.student_email,b.student_address,b.course_name from payment_details a, student_details b where a.student_id=b.id and a.receipt_no=%s"
            cursor.execute(query, [qreceipt])
            rows = cursor.fetchall()
        for row in rows:
            name = row[4]
            email = row[6]
            phone = row[5]
            address = row[7]
            course_name = row[8]
            fee_paid = row[0]
            payment_mode = row[1]
            payment_date = row[2]
            receipt = row[3]

        gst_rate = 0.18
        rate, cgst, sgst = calculate_components(fee_paid, gst_rate)

        context = {
            'name': name,
            'email': email,
            'mobile': phone,
            'address': address,
            'course_name': course_name,
            'fee_paid': fee_paid,
            'payment_mode': payment_mode,
            'rate': rate,
            'cgst': cgst,
            'sgst': sgst,
            'receipt': receipt,
            'paid_on': payment_date
        }
        filename = 'Receipt_' + name
        return render_to_pdf('receipt.html', filename, context)
    else:
        return render(request, 'student_receipt/reGenerateReceipt.html')