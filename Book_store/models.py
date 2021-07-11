from django.db import models
from django.contrib.auth.models import User
import datetime
import math
from django.utils import timezone
# Create your models here.
# class customer(models.Mode):
#     first_name=models.CharField(max_length=100)
#     last_name =models.CharField(max_length=100)
class Books(models.Model):
    book_name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    publication=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    rating=models.PositiveIntegerField()
    available=models.BooleanField(default=True)

    def __str__(self):
        return self.book_name
class IssueBook(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(Books,on_delete=models.CASCADE)
    issue_date=models.DateTimeField()
    return_date=models.DateTimeField(default=timezone.now())
    returned=models.BooleanField(default=False)

    @property
    def RetDate(self):
        self.return_date1=self.issue_date+datetime.timedelta(days=30)
        return self.return_date1
    @property
    def fined(self):
        if self.return_date> self.RetDate:
            no_of_days = self.return_date-self.RetDate
            self.fine = 2*no_of_days.days
            return self.fine
# class Fine(models.Model):
#     fined_user=models.
#     fined=models.BooleanField()
#     fine=models.PositiveIntegerField()
