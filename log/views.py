from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required(login_url="login/")

def home(request):
    return render(request,"home.html")
def LoginRequest(request):
    active = "index"
    message = ""
    if request.user.is_authenticated():
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = authenticate(username=username,password=password)
                if user is not None and user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('contact'))
                else:
                    message = "user and/or password incorrect"


    ctx = {'active':active, 'form': form}
    return render_to_response('home',{'FORM':form,'ERROR':error},context_instance=RequestContext(request))
    
def LogoutRequest(request):
    return redirect('LoginForm')
