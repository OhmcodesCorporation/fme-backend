from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.sites.shortcuts import get_current_site
from django.views.generic import TemplateView

from .forms import *
from .models import *
from .email import send_confirmation_email
from .tokens import token_gen 


class HomeView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ThanksView(TemplateView):
    template_name = 'thanks.html'


def ProfileView(request):
    if request.user.is_authenticated():
        context = {'usr_info':request.user}
        return render(request, 'profile.html',context)
    else:
        return redirect('index')

def contactus(request):
    if request.method == 'POST':
        form = contactUsForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            from_email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            template = get_template('contactUs_template.txt')
            content = template.render({'subject': subject, 'from_email': from_email, 'message': message,})
            send_mail(subject, content, from_email, ['administrator@count-down-marketplace.com',])
            messages.success(request, 'Your thoghts have been colected, We will contact you if required. Thank you!')
            return redirect('login')

    else:
        form = contactUsForm()
    return render(request, 'contact.html',{'form': form})

def CreateUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            current_site = get_current_site(request)
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('user_name')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            pwd_hash = make_password(raw_password)
            #Save to User table
            new_user = User(username=username,first_name=firstname,last_name=lastname,email=email,password=pwd_hash)
            if not User.objects.filter(username=username).exists():
                new_user.is_active = False
                new_user.save()

                #Save to Profile Table
                # pr = Profile(fnme=firstname ,lnme=lastname , mnme=middlename ,usrn=username,
                # pwd=pwd_hash,emladdress=email,address=address,dob=birth_date)
                # pr.save()

                send_confirmation_email(new_user, current_site, email)
                messages.success(request, 'Congratulations! Email has been sent to your provided email account for confirmation!')
                return redirect('login')
            else:
                messages.info(request, "Username taken!")
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})
 
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        #For auto login after activate uncomment below
        #login(request, user)
        messages.success(request, 'Thank you for confirming your email address!')
        return redirect('login')

    else:
        messages.error(request, 'OHH NO! The confirmation link is invalid or has expired.')
        return redirect('login')

