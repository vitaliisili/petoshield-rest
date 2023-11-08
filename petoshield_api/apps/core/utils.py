from django.core.mail import send_mail
from django.contrib.sites.models import Site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator


from apps.user.models import User, MailVerificationTokens # Just for testing purposes

def generate_token(user: User):
    """Token generator"""
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    
    return token, uid


def send_confirmation_email(user_profile: User):
    """Email confirmation function"""
    
    site = Site.objects.get_current()
    token = MailVerificationTokens.objects.get(user=user_profile.pk)
    confirmation_link = f"http://{site.domain}/confirm-email/{token.confirmation_token}/"

    subject = "Please, confirm your email"
    message = f"Please click the following link to confirm your email address: {confirmation_link}"

    send_mail(
        subject, 
        message, 
        "timoschulz306@gmail.com", 
        [user_profile.user.email]
    )
