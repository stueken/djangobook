import datetime

from django.db import models
from django.utils import timezone


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


class Author(models.Model):
    salutation = models.CharField(max_length=10, default="Hello")
    name = models.CharField(max_length=200, default="No Name")
    email = models.EmailField(blank=True)
    headshot = models.ImageField(upload_to='author_headshots', blank=True)
    last_accessed = models.DateTimeField()

    def __str__(self):
        return self.name


class BookManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()


class DahlBookManager(models.Manager):
    def get_queryset(self):
        return super(DahlBookManager, self).get_queryset().filter(
            author='Roald Dahl')


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True)
    num_pages = models.IntegerField(blank=True, null=True)
    objects = BookManager()  # the default manager
    dahl_objects = DahlBookManager()  # The Dahl-specific manager

    def __str__(self):
        return self.title

    def recent_publication(self):
        return self.publication_date >= timezone.now().date() - datetime.timedelta(weeks=8)
