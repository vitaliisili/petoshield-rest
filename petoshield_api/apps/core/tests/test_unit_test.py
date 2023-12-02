from django.core import mail
from django.template.loader import get_template


class TestEmailSender:

    def test_mail_send_confirmation_email(self, simple_user, confirmation_token, settings, email_sender):
        remote = 'http://example.com/'
        confirmation_link = f"{remote}confirm-email/?token={confirmation_token.confirmation_token}"
        subject = "Please, confirm your email"
        message = f"Please click the following link to confirm your email address: {confirmation_link}"
        expected_email = mail.EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [simple_user.email],
        )

        email_sender.send_confirmation_email(simple_user, remote)

        assert len(mail.outbox) == 1
        assert mail.outbox[0].subject == expected_email.subject
        assert mail.outbox[0].from_email == expected_email.from_email
        assert mail.outbox[0].to == expected_email.to

    def test_mail_send_password_reset_email(self, simple_user, confirmation_token, settings, email_sender):
        redirect_link = 'http://example.com/reset-password'
        link = f'{redirect_link}?token={confirmation_token.confirmation_token}'
        subject = "Reset Password"
        message = f"Please click the following link to reset your password: {link}"
        expected_email = mail.EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [simple_user.email],
        )

        email_sender.send_password_reset_email(simple_user, redirect_link)

        assert len(mail.outbox) == 1
        assert mail.outbox[0].subject == expected_email.subject
        assert mail.outbox[0].from_email == expected_email.from_email
        assert mail.outbox[0].to == expected_email.to

    def test_mail_send_mail_checkout_confirm(self, email_invoice_data, settings, email_sender):
        subject = 'Payment Confirmation and Policy Validity'
        template_path = './emails/checkout_confirm_email.txt'
        context = {
            'email': email_invoice_data['email'],
            'invoice_url': email_invoice_data['invoice_url'],
        }
        email_text = get_template(template_path).render(context)
        expected_email = mail.EmailMessage(
            subject,
            email_text,
            settings.EMAIL_HOST_USER,
            [email_invoice_data['email']],
        )

        email_sender.send_mail_checkout_confirm(email_invoice_data)

        assert len(mail.outbox) == 1
        assert mail.outbox[0].subject == expected_email.subject
        assert mail.outbox[0].body == expected_email.body
        assert mail.outbox[0].from_email == expected_email.from_email
        assert mail.outbox[0].to == expected_email.to

    def test_mail_send_mail_subscription_cancelled(self, email_data, settings, email_sender):
        subject = f'Notice of Policy Cancellation: {email_data["policy_number"]}'
        template_path = './emails/policy_cancelled_email.txt'
        context = {
            'name': email_data['name'],
            'email': email_data['email'],
            'policy_number': email_data['policy_number'],
        }
        email_text = get_template(template_path).render(context)
        expected_email = mail.EmailMessage(
            subject,
            email_text,
            settings.EMAIL_HOST_USER,
            [email_data['email']],
        )

        email_sender.send_mail_subscription_cancelled(email_data)

        assert len(mail.outbox) == 1
        assert mail.outbox[0].subject == expected_email.subject
        assert mail.outbox[0].body == expected_email.body
        assert mail.outbox[0].from_email == expected_email.from_email
        assert mail.outbox[0].to == expected_email.to
