from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # NOTE: @property allows the method to be called without parens
    # This is a neat little method nested in models that concatenates first and last name
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"