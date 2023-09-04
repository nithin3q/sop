from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import EffizientForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


# Create your views here.
def home(request):
    form = EffizientForm()
    
    if request.method == "POST":
        form = EffizientForm(request.POST)

        if form.is_valid():
            form.save()

            subject = "Acknowledgement of Form Submission"
            message_context = {'email':form.cleaned_data['email'], 
                               'full_name':form.cleaned_data['full_name'], 
                               'age':form.cleaned_data['age'], 
                               'education':form.cleaned_data['education'], 
                               'institute_of_highest':form.cleaned_data['institute_of_highest'], 
                               'course_of_study':form.cleaned_data['course_of_study'],
                               'work_experience':form.cleaned_data['work_experience'], 
                               'institute_canada':form.cleaned_data['institute_canada'], 
                               'study_in_canada':form.cleaned_data['study_in_canada'], 
                               'country_applying_from':form.cleaned_data['country_applying_from'],
                               'future_goals':form.cleaned_data['future_goals'], 
                               'english_scores_listening': form.cleaned_data['english_scores_listening'], 
                               'english_scores_reading': form.cleaned_data['english_scores_reading'],
                               'english_scores_speaking': form.cleaned_data['english_scores_speaking'],
                               'english_scores_writing': form.cleaned_data['english_scores_writing'],
                               'first_year_tuition': form.cleaned_data['first_year_tuition'], 
                               'tuition_fee': form.cleaned_data['tuition_fee'], 
                               'GIC': form.cleaned_data['GIC'], 
                               'cost_of_gic': form.cleaned_data['cost_of_gic']

            }
            message = render_to_string('email/email.html', message_context)
            recipient_list = [form.cleaned_data['email'],]
            #from_email = settings.EMAIL_HOST_USER #uncomment this line for production
            from_email = 'test@gmail.com' #comment this line for production
            try:
                email = EmailMessage(subject, message, from_email, recipient_list)
                email.content_subtype = "html"
                email.send()
            except:
                return HttpResponse('Email was not sent, an unknown error occured.')

            return redirect('success')

    context= {'form':form}


    return render (request, 'core/index.html', context)

def success(request):
    return render(request, 'core/success.html')