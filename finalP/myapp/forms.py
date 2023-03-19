from django import forms


class AddCredit(forms.Form):
    amount = forms.DecimalField(
        label='Amount', min_value=0, max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'autofocus': True}))
    transaction_type = forms.ChoiceField(
        choices=[('deposit', 'Deposit'), ('withdraw', 'Withdraw')], widget=forms.Select(attrs={'class': 'form-control form-floating form-select'}))
