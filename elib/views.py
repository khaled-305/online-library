from django.shortcuts import render, get_object_or_404
from elib.models import Genre, Book, BookInstance, Author, Language
from django.views import generic

# Create your views here.

def index(request):
	num_books = Book.objects.all().count()
	num_bookinstance = BookInstance.objects.all().count()
	num_instances_avaliable = BookInstance.objects.filter(status__exact='a').count()
	num_authors = Author.objects.all().count()
	num_visits = request.session.get('num_visits', 1) 
	request.session['num_visits'] = num_visits + 1

	context = {
	'num_books': num_books,
	'num_bookinstances': num_bookinstance,
	'num_instances_avaliable': num_instances_avaliable,
	'num_authors': num_authors,
	'num_visits': num_visits
	}

	return render(request, 'elib/index.html', context)

class BookListView(generic.ListView):
	model = Book

def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'elib/book_detail.html', context={'book': book})

class AuthorListView(generic.ListView):
	model = Author

def author_detail_view(request, pk):
	author = get_object_or_404(Author, pk=pk)
	
	context = {
	'author': author
	}
	return render(request, 'elib/author_detail.html', context)
