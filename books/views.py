from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views.generic import DetailView, ListView

from books.models import Author, Book, Publisher


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {
                'books': books, 'query': q})
    return render(request, 'search_form.html', {'errors': errors})


class PublisherList(ListView):
    model = Publisher
    context_object_name = 'my_favorite_publishers'


class PublisherDetail(DetailView):
    model = Publisher  # queryset = Publisher.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context


class BookList(ListView):
    queryset = Book.objects.order_by('-publication_date')
    context_object_name = 'book_list'


class AcmeBookList(ListView):
    context_object_name = 'book_list'
    queryset = Book.objects.filter(publisher__name='Acme Publishing')
    template_name = 'books/acme_list.html'


class PublisherBookList(ListView):
    template_name = 'books/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.args[0])
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherBookList, self).get_context_data(**kwargs)
        # Add in the publisher
        context['pbulisher'] = self.publisher
        return context


class AuthorDetailView(DetailView):
    queryset = Author.objects.all()

    def get_object(self):
        # Call the superclass
        object = super(AuthorDetailView, self).get_object()

        # Record the last accessed date
        object.last_accessed = timezone.now()
        object.save()
        # Return the object
        return object
