import datetime

from django.core import mail
from django.core.management import call_command
from django.test import TestCase
from django.utils import timezone
from django.utils.six import StringIO

from .models import Book


# Create your tests here.
class BookMethodTests(TestCase):

    def test_recent_pub(self):
        """ recent_publication() should return False for future publication
        dates.
        """

        futuredate = timezone.now().date() + datetime.timedelta(days=5)
        future_pub = Book(publication_date=futuredate)
        self.assertEqual(future_pub.recent_publication(), False)


class EmailTest(TestCase):
    def test_send_email(self):
        # Send message.
        mail.send_mail('Subject here', 'Here is the message.',
                       'from@example.com', ['to@example.com'],
                       fail_silently=False)

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'Subject here')


class ClosepollTest(TestCase):
    def test_command_output(self):
        out = StringIO()
        call_command('closepoll', stdout=out)
        self.assertIn('Expected output', out.getvalue())
