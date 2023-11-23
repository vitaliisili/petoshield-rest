from django.core.mail import send_mail
from django.template.loader import get_template
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
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )

    @staticmethod
    def send_welcome_email(user):
        subject = 'Welcome to Petoshield Pet Insurance - Your Partner in awesome Protection!'
        template_path = './emails/welcome_email.txt'
        context = {'name': user.name}
        email_text = get_template(template_path).render(context)

        send_mail(
            subject=subject,
            message=email_text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
        )

    @staticmethod
    def send_welcome_email_for_service_provider(user):
        subject = "Welcome to Petoshield Pet Insurance - Your Partner in awesome Protection!"
        template_path = './emails/welcome_service_provider_email.txt'
        context = {'name': user.name}
        email_text = get_template(template_path).render(context)

        send_mail(
            subject=subject,
            message=email_text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )

    @staticmethod
    def send_reset_password_warning_email(user):
        subject = "Subject: Notification: Password Change Request"
        template_path = './emails/password_is_changed_email.txt'
        context = {'name': user.name}
        email_text = get_template(template_path).render(context)

        send_mail(
            subject=subject,
            message=email_text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )

    @staticmethod
    def send_mail_your_ticket_received(email_data):
        subject = 'Thank you for your interest'
        template_path = './emails/ticket_received_email.txt'
        context = {'name': email_data['name']}
        email_text = get_template(template_path).render(context)

        send_mail(
            subject=subject,
            message=email_text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email_data["email"]],
        )

    @staticmethod
    def send_mail_job_ticket_received(email_data):
        subject = f'Thank you for your Job Application for position of {email_data["position"]}'
        template_path = './emails/job_ticket_received_email.txt'
        context = {
            'name': email_data['name'],
            'position': email_data['position'],
        }
        email_text = get_template(template_path).render(context)

        send_mail(
            subject=subject,
            message=email_text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email_data["email"]],
        )

    @staticmethod
    def send_mail_partner_ticket_received(email_data):
        subject = 'Exploring Partnership Opportunities with Petoshield Pet Insurance'
        template_path = './emails/partner_ticket_received_email.txt'
        context = {
            'name': email_data['name'],
            'business_name': email_data['business_name'],
        }
        email_text = get_template(template_path).render(context)

        send_mail(
            subject=subject,
            message=email_text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email_data["email"]],
        )

    @staticmethod
    def send_mail_checkout_confirm(email_data):
        subject = 'Payment Confirmation and Policy Validity'
        template_path = './emails/checkout_confirm_email.txt'
        context = {
            'name': email_data['name'],
            'email': email_data['email'],
            'policy_number': email_data['policy_number'],
            'invoice_id': email_data['invoice_id'],
            'invoice_url': email_data['invoice_url'],
        }
        email_text = get_template(template_path).render(context)

        send_mail(
            subject=subject,
            message=email_text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email_data["email"]],
        )

    @staticmethod
    def send_mail_subscription_cancelled(email_data):
        subject = f'Notice of Policy Cancellation: {email_data["policy_number"]}'
        template_path = './emails/policy_cancelled_email.txt'
        context = {
            'name': email_data['name'],
            'email': email_data['email'],
            'policy_number': email_data['policy_number'],
        }

        email_text = get_template(template_path).render(context)

        send_mail(
            subject=subject,
            message=email_text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email_data["email"]],
        )

    @staticmethod
    def send_mail_account_deleted(email_data):
        subject = 'Notice: Account Deletion'
        template_path = './emails/delete_account_email.txt'
        context = {
            'name': email_data['name'],
            'email': email_data['email'],
        }
        email_text = get_template(template_path).render(context)

        send_mail(
            subject=subject,
            message=email_text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email_data["email"]],
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
    def password_validation(raw_password):
        try:
            validate_password(raw_password)
        except ValidationError as error:
            raise RestValidationError(error)
