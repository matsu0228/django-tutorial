import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Post

class BlogTests(TestCase):
    def test_publish_date(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        future_time = timezone.now() + datetime.timedelta(days=30)
        future_post = Post(published_date=future_time)
        self.assertIs(future_post.was_published_recently(), False)
