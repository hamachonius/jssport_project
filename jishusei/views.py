from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Jishusei
# Create your views here.
@login_required
def create (request):
    if requested.method == 'POST':
        if request.POST['name'] and request.POST['introduction'] and request.POST['url'] and request.FILES['image'] and request.POST['location']:
           company = Company()
           company.name = request.POST['name']
           company.introduction = request.POST['introduction']
           if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
               company.url = request.POST['url']
           else:
               company.url = 'http://' + request.POST['url']
           company.image = request.FILES['image']
           company.regi_date = timezone.datetime.now()
           company.companyid = request.user
           company.save()
           return redirect('home')
        else:
           return render(request, 'company/create.html',{'error':'All fields are required.'})
    else:
        return render(request, 'company/registercompany.html')
