from django.shortcuts import render
from .models import Phone

# Create your views here.

def list(request):
    phones = Phone.objects.all().order_by('name')
    return render(request, 'contacts/list.html', {'phones' : phones})
