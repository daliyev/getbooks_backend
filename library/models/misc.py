from django.db import models
from .book import Book
from django.contrib.auth import get_user_model
User = get_user_model()


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    rating = models.PositiveIntegerField()
    date_posted = models.DateField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,  related_name='reviews')


class LikedBook(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Notification(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = models.TextField()
    type = models.CharField(max_length=250)
    sent_at = models.DateField(auto_now_add=True)


class BookActions(models.Model):
    view_count = models.PositiveIntegerField(default=0)
    download_count = models.PositiveIntegerField(default=0)
    book = models.OneToOneField(Book, primary_key=True, on_delete=models.PROTECT)

    def get_view_count(self):
        return self.view_count

    def get_download_count(self):
        return self.download_count

    def get_full_actions(self):
        act = {
            "view_count": self.view_count,
            "download_count": self.download_count
        }
        return act


class BookViewHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
