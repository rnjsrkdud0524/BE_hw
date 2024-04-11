from django.shortcuts import render
from .models import Phone
from django.views.generic import ListView

# Create your views here.

# def list(request):
#    phones = Phone.objects.all().order_by('name')
#    return render(request, 'contacts/list.html', {'phones' : phones})

def result(request):
    entered_text = request.GET['name']
    phones = Phone.objects.all().order_by('name')
    name = Phone.objects.filter(name__contains=entered_text)

    return render(request, "contacts/result.html", {'phones' : phones, 'alltext' : entered_text, 'name' : name})

class IndexView(ListView):
    queryset = Phone.objects.all().order_by('name')
    template_name = 'contacts/list.html'
    context_object_name = 'phones'