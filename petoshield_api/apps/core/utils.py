from django.core.mail import send_mail
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework.exceptions import ValidationError as RestValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from apps.user.models import User, MailVerificationTokens
import uuid
from config import settings


class EmailSender:

    @staticmethod
    def send_confirmation_email(user: User, remote):
        """Email confirmation function"""

        token = uuid.uuid4()
        confirmation_link = f"{remote}confirm-email/?token={token}"
        # confirmation_link = 'https://example.com'

        MailVerificationTokens.objects.create(user=user, confirmation_token=token, )

        subject = "Please, confirm your email"
        message = f"Please click the following link to confirm your email address: {confirmation_link}"

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email]
        )

    @staticmethod
    def send_password_reset_email(user, redirect_link):
        token = uuid.uuid4()
        MailVerificationTokens.objects.create(user=user, confirmation_token=token)

        link = f'{redirect_link}?token={token}'

        subject = "Reset Password"
        message = f"Please click the following link to reset your password: {link}"

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email]
        )

    @staticmethod
    def send_welcome_email(user):
        subject = "Welcome to Petoshield Pet Insurance - Your Partner in awesome Protection!"
        message = f'''
Dear {user.name},

Welcome to Petoshield Pet Insurance – where we're dedicated to providing you and your furry family members with the
perfect coverage for a lifetime of tail-wagging and whisker-twitching adventures!

We're thrilled to have you on board and want to express our heartfelt thanks for choosing Petoshield as your trusted
partner in pet insurance. We understand that your pets are more than just animals; they're cherished members of your
family, and their health and happiness are of utmost importance.

Here's what you can expect from your Petoshield Pet Insurance:

1. Comprehensive Coverage: Our insurance plans are designed to provide extensive coverage for veterinary expenses,
 ensuring that your pet receives the best medical care when they need it most.

2. Simple and Transparent: We believe in making pet insurance straightforward. No hidden clauses or complicated
jargon – just clear, transparent policies to give you peace of mind.

3. Fast Claims Processing: We understand that when your pet is unwell, time is of the essence. Our streamlined
claims process ensures that you get reimbursed quickly, so you can focus on what matters most – your pet's well-being.

4. Pet Wellness Resources: Stay informed and proactive about your pet's health with our exclusive wellness resources.
From preventive care tips to helpful articles, we're here to support you in keeping your pet happy and healthy.

5. If you have any questions, need assistance, or simply want to share a delightful pet story, our customer support
team is here for you. Reach out to us at petoshield@gmail.com.

6. Thank you for entrusting Petoshield with the care of your beloved pets. We look forward to being your go-to partner
in ensuring a lifetime of joy and well-being for your furry companions.

Warm regards,
The Petoshield Pet Insurance Team'''

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email]
        )


class JwtToken:

    @staticmethod
    def get_jwt_token(user: User) -> dict:
        jtw_token = RefreshToken.for_user(user)
        response = {
            'access': str(jtw_token.access_token),
            'refresh': str(jtw_token)
        }
        return response


class Validate:
    
    @staticmethod
    def password_validation(request):
        try:
            validate_password(request.data.get('password'))
        except ValidationError as error:
            raise RestValidationError(error)
    
