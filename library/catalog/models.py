from django.db import models

class Books(models.Model):
    Loaned = 'l'
    Available = 'a'
    Avail = (
        (Loaned, 'Loaned'),
        (Available, 'Available')
    )
    fieldsets = (
        ('Available', {
            'fields': ('available', 'return_d')
        })
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    available = models.CharField(max_length=2, default='a', choices= Avail)
    return_d = models.DateTimeField('Date of return',default='')

class Issues(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    issue = models.DateTimeField('Date issued')
    return_d = models.DateTimeField('Date of return')

class Students(models.Model):
    s_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=10)
    loans = models.CharField(max_length=200)

all_books = Books.objects.all()

def __str__(self):
 """
 String for representing the Model object.
 """
 return self.Books.title
    
    
def get_absolute_url(self):
 """
 returns the url to access a particular book instance.
 """
 return reverse('available', args=[str(self.id)])

Avail = (
        ('l', 'On loan'),
        ('a', 'Available')
 )

status = models.CharField(max_length=1, choices=Avail, blank=True, default='a', help_text='Book availability')

class Meta:
 ordering = ["return_d"]
        

def __str__(self):
 """
 String for representing the Model object
 """
 return '{0} ({1})'.format(self.Books.title)
