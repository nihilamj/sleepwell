from django.core.mail import send_mail
from django.template.loader import render_to_string 
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives


from_email = "vbuild64@gmail.com"

def otpmail(email,otp,stage,name):
    if stage == 'reset_password':
        html_template = 'healthprofile/mails/reset_password.html'
        context = None
        subject = "SLEEPWELL -  OTP for Password Reset"
        recipient_list = [email]

        context = {'OTP':otp,'name':name}
        html_message = render_to_string(html_template, {'context':context})

        msg = EmailMessage(subject, html_message, from_email, recipient_list)
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()
    
    if stage == 'activation':
        html_template = 'healthprofile/mails/activation.html'
        context = None
        subject = "SLEEPWELL - Activate Your SleepWell Account"
        recipient_list = [email]

        context = {'OTP':otp,'name':name}
        html_message = render_to_string(html_template, {'context':context})

        msg = EmailMessage(subject, html_message, from_email, recipient_list)
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()

    # subject = "PASSWORD RESET"
    # message = "OTP for password reset = "+otp+" ."
    
    # recipient_list = [email]
    # send_mail(subject,message,from_email,recipient_list)