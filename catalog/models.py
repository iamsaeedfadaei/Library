from django.db import models
from django.urls import reverse
import uuid





class Genre(models.Model):
    name = models.CharField(max_length=20, help_text='Enter the Book Genre Please')

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'



class Book(models.Model):
    title = models.CharField(max_length=50, help_text='Enter the Book Title Please')
    isbn = models.CharField(
        'ISBN',max_length=13, 
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre, help_text='Please Select the Book Genre')
    summary = models.TextField(help_text='Enter a brief description of the Book')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('book', args=[str(self.id)])

    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'




class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    # book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book Availability')

    class Meta:
        ordering = ['due_back']
    
    def __str__(self):
        return f'{self.id} (self.book.title)'






