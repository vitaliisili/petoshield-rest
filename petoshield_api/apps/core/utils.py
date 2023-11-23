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

    @staticmethod
    def send_welcome_email_for_service_provider(user):
        subject = "Welcome to Petoshield Pet Insurance - Your Partner in awesome Protection!"
        message = f'''

Dear {user.name},

We hope this email finds you well. On behalf of the entire Petoshield Insurance team, we extend a warm welcome to you
as our newest registered service provider. We are thrilled to have you on board and look forward to a successful
partnership in providing top-notch services to our valued customers.

At Petoshield, we are dedicated to offering comprehensive insurance coverage for pets, ensuring the health and
well-being of our customers' beloved companions. Your role as a service provider is integral to this mission, and we
are confident that your expertise will contribute significantly to the satisfaction and peace of mind of our
policyholders.

Here are a few key points to get you started:

1. Profile Setup: Please take a moment to review and complete your service provider profile on our platform. Ensure that
all relevant information, including contact details and services offered, is accurate and up to date.

2. Insurance Claims: As a registered service provider, you may be involved in processing insurance claims related to pet
care. Familiarize yourself with our claims procedures, and feel free to reach out to our dedicated support team for any
assistance.

3. Communication: Clear communication is essential for a successful partnership. If you have any questions, concerns, or
if there are updates to your services, please keep us informed. We value transparency and collaboration.

4. Training and Resources: Stay tuned for any training sessions, updates, or resources that we provide to enhance your
understanding of our insurance processes and to improve the overall customer experience.

Once again, welcome to the Petoshield Insurance family. We are excited about the opportunities that lie ahead and are
confident that together, we can make a positive impact on the lives of pets and their owners.

If you have any immediate questions or if there is anything we can assist you with, please don't hesitate to contact
our support team at petoshield@gmail.com

Thank you for choosing Petoshield Insurance. We look forward to a successful partnership!

Warm regards,
The Petoshield Pet Insurance Team'''

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email]
        )

    @staticmethod
    def send_reset_password_warning_email(user):
        subject = "Subject: Notification: Password Change Request"
        message = f'''
Dear {user.name},

I trust this email finds you well.

We wanted to bring to your attention that there has been a recent attempt to change the password associated with your
account on our platform. The security of your account is of utmost importance to us, and we take every measure to
ensure its protection.

If you initiated this password change request, please disregard this message. However, if you did not make this
request, we strongly recommend taking immediate action to secure your account.

Here are a few steps you can take:

1. Reset Your Password: Visit our website and initiate a password reset. Choose a strong and unique password that
includes a combination of letters, numbers, and special characters.

2. Enable Two-Factor Authentication (2FA): For an added layer of security, consider enabling two-factor authentication
on your account.

3. Review Account Activity: Check your account activity for any unauthorized access or suspicious activities. If you
notice anything unusual, please contact our support team immediately.

If you need any assistance or have concerns about the security of your account, feel free to reach out to our support
team at petoshield@gmail.com.

Thank you for your prompt attention to this matter. We appreciate your cooperation in helping us maintain the security
of your account.

Best regards,
The Petoshield Pet Insurance Team'''

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email]
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
    def send_mail_saccount_deleted(email_data):
        subject = f'Notice: Account Deletion'
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
