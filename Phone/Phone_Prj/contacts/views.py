from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone
from django.views.generic import ListView
from django.shortcuts import render

# Create your views here.

def list(request):
    phones = Phone.objects.all().order_by('name')
    return render(request, 'contacts/list.html', {'phones' : phones})

def result(request):
    entered_text = request.GET['name']
    phones = Phone.objects.all().order_by('name')
    name = Phone.objects.filter(name__contains=entered_text)

    return render(request, "contacts/result.html", {'phones' : phones, 'alltext' : entered_text, 'name' : name})

class IndexView(ListView):
    queryset = Phone.objects.all().order_by('name')
    template_name = 'contacts/list.html'
    context_object_name = 'phones'

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone_num = request.POST.get('phone_num')
        email = request.POST.get('email')

        post = Phone.objects.create(
            name = name,
            phone_num = phone_num,
            email = email
        )
        return redirect('list')
    
    return render(request, 'contacts/create.html')

def detail(request, id):
    contact = get_object_or_404(Phone, id = id)
    return render(request, 'contacts/detail.html', {'contact' :contact})

def update(request, id):
    contact = get_object_or_404(Phone, id = id)
    if request.method == "POST":
        contact.name = request.POST.get('name')
        contact.phone_num = request.POST.get('phone_num')
        contact.email = request.POST.get('email')
        contact.save()
        return redirect('list')
    return render(request, 'contacts/update.html', {'contact' :contact})


def delete(request, id):
    contact = get_object_or_404(Phone, id = id)
    if request.method == "POST":
        contact.delete()
        return redirect('list')
    return render(request, 'contacts/delete.html', {'contact' :contact})