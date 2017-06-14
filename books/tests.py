import datetime

from django.test import TestCase
from django.utils import timezone

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
