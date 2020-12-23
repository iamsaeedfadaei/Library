from django.shortcuts import render, HttpResponse
from django.views import generic
from .models import Book, BookInstance, Author, Genre



def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_available_instances = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()
    num_genres = Genre.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_available_instances': num_available_instances,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_visits': num_visits,
    }

    return render(request, 'catalog/index.html', context)




class BookListView(generic.ListView):
    model = Book
    # queryset = Book.objects.filter(title__icontains='django')
    context_object_name = 'book_list'
    template_name = 'catalog/book_listings.html'
    paginate_by = 2

    

class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'catalog/book_detail.html'



class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'
    template_name = 'catalog/author_listings.html'




class AuthorDetailView(generic.DeleteView):
    model = Author
    context_object_name = 'author'
    template_name = 'catalog/author_detail.html'