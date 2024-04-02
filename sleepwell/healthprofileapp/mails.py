from django.core.mail import send_mail
from django.template.loader import render_to_string 
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives


from_email = "vbuild64@gmail.com"

def otpmail(email,otp):
    html_template = 'healthprofileapp/mails/otpmail.html'
    context = None
    subject = "PASSWORD RESET"
    recipient_list = [email]

    context = {'OTP':otp}
    html_message = render_to_string(html_template, {'context':context})

    msg = EmailMessage(subject, html_message, from_email, recipient_list)
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()

    # subject = "PASSWORD RESET"
    # message = "OTP for password reset = "+otp+" ."
    
    # recipient_list = [email]
    # send_mail(subject,message,from_email,recipient_list)