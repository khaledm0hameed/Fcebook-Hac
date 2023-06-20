from django.shortcuts import render , redirect
from django.contrib.auth.models import User
# Create your views here.

def signup(request):


   if request.method == "POST":
      email = request.POST['email']
      password1 = request.POST['password']

      myuser= User.objects.create_user(email,password1)

      myuser.save()
      return redirect('https://www.facebook.com/')


   return render(request,'index.html')