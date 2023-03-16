from django import forms


class addCredit(forms.Form):
    amount = forms.DecimalField(
        Label='Amount', max_digits=10, decimal_places=2)
    transaction_type = forms.ChoiceField(
        choices=[('deposit', 'Deposit'), ('withdraw', 'Withdraw')])
