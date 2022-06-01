from django.core.mail import send_mail

def send_activate_code(activate_code, email:str):
    
    title = 'Hey there! It is a link for activating your acc on the HW_SHOP'
    message = f'Please click the link to activate your acc http://127.0.0.1:8000/api/v1/account/activate/{activate_code}/'
    sender = 'babulekh010@gmail.com'

    send_mail(
        title,
        message,
        sender,
        [email],
        fail_silently=False,
    )