from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Username:{self.username}, Balance:{self.balance}"


# class Credit(models.Model):
#     username = models.OneToOneField(
#         User, on_delete=models.CASCADE, related_name="account_user")
#     balance = models.IntegerField(default=0)

#     def __str__(self):
#         return f"{self.username} has {self.balance} in Balance"
