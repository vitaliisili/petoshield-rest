from django.core.mail import send_mail
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

        MailVerificationTokens.objects.create(user=user, confirmation_token=token,)

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


class JwtToken:

    @staticmethod
    def get_jwt_token(user: User) -> dict:
        jtw_token = RefreshToken.for_user(user)
        response = {
            'access': str(jtw_token.access_token),
            'refresh': str(jtw_token)
        }
        return response
