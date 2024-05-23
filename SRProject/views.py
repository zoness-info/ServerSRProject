# # myapp/views.py
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.http import HttpResponseRedirect
# from SR_Plant_I.forms import CustomAuthenticationForm

# def root_login_view(request):
#     if request.method == 'POST':
#         form = CustomAuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect_to_app(user)
#     else:
#         form = CustomAuthenticationForm()
#     return render(request, 'SRPlant_I_Temp/login.html', {'form': form})


# def redirect_to_app(user):
#     if user.app1_access:
#         return HttpResponseRedirect('/app1/')
#     elif user.app2_access:
#         return HttpResponseRedirect('/app2/')
#     elif user.app3_access:
#         return HttpResponseRedirect('/app3/')
#     elif user.app4_access:
#         return HttpResponseRedirect('/app4/')
#     elif user.app5_access:
#         return HttpResponseRedirect('/app5/')
#     else:
#         return HttpResponseRedirect('/')
