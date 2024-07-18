from django.shortcuts import render
from.models import FormModel

# Create your views here.
def home_view(request):
    if request.method == "POST":
        full_name = request.POST['fullName']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        FormModel.objects.create(full_name=full_name,email=email,phone=phone,message=message)
    return render(request,'home.html')

def submited_view(request):
    display = FormModel.objects.all()
    return render(request,'submited.html',{'display':display})