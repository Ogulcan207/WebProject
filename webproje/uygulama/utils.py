import random
import string
from django.core.mail import send_mail

def generate_verification_code(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def send_verification_email(email, code):
    subject = 'Ödeme Doğrulama Kodu'
    message = f'Doğrulama kodunuz: {code}'
    from_email = 'yigit.dikbas@hotmail.com'  # Bu adres, EMAIL_HOST_USER ve DEFAULT_FROM_EMAIL ile aynı olmalıdır
    send_mail(subject, message, from_email, [email])