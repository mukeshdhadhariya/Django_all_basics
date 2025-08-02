from django.shortcuts import render
from .models import ChaiVarity,Store
from django.shortcuts import get_object_or_404
from .forms import ChaivarityFrom

# Create your views here.
def all_index(request):
    chais=ChaiVarity.objects.all()
    return render(request,'chai/all_index.html',{'chais':chais})

def chai_details(request,chai_id):
    chai=get_object_or_404(ChaiVarity,pk=chai_id)
    return render(request,'chai/chai_details.html',{'chai':chai  })

def Chai_store_view(request):
    stores=None
    if request.method=='POST':
        form=ChaivarityFrom(request.POST)
        if form.is_valid():
            chai_varity=form.cleaned_data['chai_varity']
            stores=Store.objects.filter(chai_varities=chai_varity)
    else :
        form=ChaivarityFrom()

    return render(request,'chai/Chai_stores.html',{'stores':stores,'form':form})