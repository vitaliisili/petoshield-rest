from django.core.mail import send_mail
from apps.user.models import User, MailVerificationTokens
import uuid
from config import settings


class EmailSender:

    @staticmethod
    def send_confirmation_email(user: User, remote):
        """Email confirmation function"""

        token = uuid.uuid4()
        confirmation_link = f"{remote}confirm-email/?token={token}"

        MailVerificationTokens.objects.create(user=user, confirmation_token=token)

        subject = "Please, confirm your email"
        message = f"Please click the following link to confirm your email address: {confirmation_link}"

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email]
        )
