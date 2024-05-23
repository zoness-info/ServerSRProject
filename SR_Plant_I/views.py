# myapp/views.py
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


from .forms import CustomAuthenticationForm

def root_login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            #print('login user is :', user)
            if user is not None:
                login(request, user)
                #print('user verified')
                return redirect_to_app(user)
            else:
                return HttpResponse('nouser')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'SRPlant_I_Temp/login.html', {'form': form})


def redirect_to_app(user):
    if isinstance(user, User):
        return HttpResponseRedirect('Packing/')
        #return HttpResponse ('User Found')  
    #     if user.app1_access:
    #         print(type(user.app1_access))
    #         return HttpResponse('app1.access')
    #         return HttpResponseRedirect('/app1/')
    #     elif user.app2_access:
    #         print(user.app2_access)
    #         return HttpResponseRedirect('/app2/')
    #     elif user.app3_access:
    #         print(user.app3_access)
    #         return HttpResponseRedirect('/app3/')
    #     elif user.app4_access:
    #         print(user.app4_access)
    #         return HttpResponseRedirect('/app4/')
    #     elif user.app5_access:
    #         print(user.app5_access)
    #         return HttpResponseRedirect('/app5/')
    #     else:
    #         print('instance not found')
    #         return HttpResponseRedirect('/')
    # else:
    #     # Handle the case where user is not an instance of CustomUser
    #     return HttpResponse('User Not Found')
