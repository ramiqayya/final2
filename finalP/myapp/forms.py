from django import forms


class AddCredit(forms.Form):
    amount = forms.DecimalField(
        label='Amount', min_value=0, max_digits=10, decimal_places=2)
    transaction_type = forms.ChoiceField(
        choices=[('deposit', 'Deposit'), ('withdraw', 'Withdraw')])
