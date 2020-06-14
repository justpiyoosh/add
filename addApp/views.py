from django.shortcuts import render
from addApp.forms import AddressForm
from addApp.models import Add 

# Create your views here.

def index(request):
    return render(request,'addApp/index.html',)

def addaddress(request):
    form = AddressForm()

    if request.method == 'POST':
        form = AddressForm(request.POST)

        if form.is_valid():
            form.save(commit='true')
            #print(form.cleaned_data['country'])
            return index(request)

        else:
            print("FORM INVALID!!")

    return render(request,'addApp/addaddress.html',{'form':form})

def myaddresses(request):
    alladd = Add.objects.all()
    return render(request,'addApp/myaddresses.html',{'alladd' : alladd})