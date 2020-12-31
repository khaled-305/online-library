from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Genre(models.Model):
	name = models.CharField(max_length=100, help_text='Enter a book genre eg: fiction, comedy etc')

	def __str__(self):
		return self.name

class Book(models.Model):
	title = models.CharField(max_length=100, help_text='Enter book title')
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
	summary = models.TextField(max_length=1000, help_text='Enter brief description of the book')
	isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='Enter ISBN number')
	genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
	language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
	cover_picture = models.ImageField(upload_to='media/', help_text="Upload book cover picture")

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('book-detail', args=[str(self.id)])

class BookInstance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='unique ID for a particular book')
	book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
	imprint = models.CharField(max_length=200)
	due_back = models.DateField(null=True, blank=True)

	LOAN_STATUS = (
		('m', 'Maintenance'),
		('o', 'On Loan'),
		('a', 'Avaliable'),
		('r', 'Reserved'),
	)

	status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book Avaliability')

	class Meta:
		ordering = ['-due_back']

	def __str__(self):
		return self.book

class Author(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	date_of_birth = models.DateField(null=True, blank=True)
	date_of_death = models.DateField('Died', null=True, blank=True)

	class Meta:
		ordering = ['last_name', 'first_name']

	def get_absolute_url(self):
		return reverse('author-detail', args=[str(self.id)])

	def __str__(self):
		return f'{self.first_name}, {self.last_name}'

class Language(models.Model):
	language = models.CharField(max_length=100, default='English')

	def __str__(self):
		return self.language
