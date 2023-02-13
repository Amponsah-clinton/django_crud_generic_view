from django.db import models
from django.urls import reverse


# Create your models here.
semester_choices = (
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    ("5","5"),
)

class User(models.Model):
    name = models.CharField(max_length=130)
    date = models.DateField(auto_now_add=True)
    semester = models.CharField(max_length=20, choices=semester_choices, default='1')
    age = models.IntegerField()
    
    def get_absolute_url(self):
        return reverse("detail_view", kwargs={"pk": self.pk})

    def __str__(request):
        return request.name
    