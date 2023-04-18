from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Username:{self.username}, Balance:{self.balance}"


class Wallet(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='wallets')
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.symbol} wallet for {self.user.username}"


class CoinsAmount(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='coin_amounts')
    wallet = models.ForeignKey(
        Wallet, on_delete=models.CASCADE, related_name='coins')
    amount = models.DecimalField(max_digits=20, decimal_places=4, default=0)

    def __str__(self):
        return f"{self.amount} {self.wallet.symbol} in {self.user.username}'s wallet"
