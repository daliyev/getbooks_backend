from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=256)
    about = models.TextField()
    image = models.ImageField(upload_to='publisher/img')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}  {self.is_active}"


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.is_active}"


class Author(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    about = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='author/img')
    birth_date = models.DateField()
    birth_location = models.CharField(max_length=250)
    death_date = models.DateField(null=True, blank=True)
    death_location = models.CharField(null=True, blank=True, max_length=256)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    name = models.CharField(max_length=256)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    about_book = models.TextField()
    publisher = models.ForeignKey(Publisher, models.CASCADE)
    published_year = models.DateField()
    pdf_file = models.FileField(upload_to='books/pdf')
    audio_file = models.FileField(null=True, blank=True, upload_to='books/audio')
    image = models.ImageField(upload_to='books/image')
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"

    def is_have(self):
        return bool(self.audio_file.name)
