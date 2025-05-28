from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'qamqor/index.html')

def about(request):
    return render(request, 'qamqor/about.html')

def appraisals(request):
    return render(request, 'qamqor/appraisals.html')

def brokerage(request):
    return render(request, 'qamqor/brokerage.html')

def consulting(request):
    return render(request, 'qamqor/consulting.html')

def contact(request):
    if request.method == "POST":
        contact_fname = request.POST['fname']
        contact_lname = request.POST['lname']
        contact_email = request.POST['email']
        contact_message = request.POST['message']

        send_mail(
            contact_fname, 
            contact_message,
            contact_email,
            ['admin@qamqorqas.com'],
            fail_silently = False,
        )


        return render(request, 'qamqor/contact.html', {'contact_fname' : contact_fname})


    else:
        return render(request, 'qamqor/contact.html')
