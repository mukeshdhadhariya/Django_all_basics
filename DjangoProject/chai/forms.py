from django import forms
from .models import ChaiVarity

class ChaivarityFrom(forms.Form):
    chai_varity = forms.ModelChoiceField(
        queryset=ChaiVarity.objects.all(),
        label='Select Chai',
        widget=forms.Select(attrs={
            'class': 'bg-black text-white border border-gray-600 rounded p-2 w-full'
        })
    )
