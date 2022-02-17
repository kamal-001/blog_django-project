from django.utils.timezone import now
from django.utils import timezone
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from home.models import Contact
# Create your views here.

def index(request): 
    allPosts= Post.objects.filter(timeStamp=timezone.now()).reverse()[:3]
    context={'allPosts': allPosts}
    return render(request, 'home/index.html', context)

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")

def about(request): 
    return render(request, 'home/about.html')

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        # lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('index')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('index')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('index')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        # myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('index')

    else:
        return HttpResponse("404 - Not found")

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("index")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("index")

    return HttpResponse("404- Not found")
   

    return HttpResponse('login')

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("index")