from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import ProfileUpdateform, Signupform, UserUpdateForm
from django.contrib.auth.password_validation import validate_password
from django.views.generic import DetailView,UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseForbidden

# Create your views here.
def signup_view(request):
    context={}
    signup_form=Signupform(request.POST or None)
    context["form"]=signup_form
    if(request.method=="POST"):  
        # print(signup_form.is_valid())
        # print(signup_form.errors)
        if(signup_form.is_valid()):
            formdata=signup_form.cleaned_data
            try:
                validate_password(formdata.get("password"))
            except ValidationError as e:
                signup_form.add_error("password",e)
                context["form"]=signup_form
                return render(request,"signup.html",context) 
            upass = signup_form.save(commit=False)
            upass.set_password(signup_form.cleaned_data['password'])
            signup_form.save()
            messages.success(request,f"Account Created for User {signup_form.cleaned_data['username']}")
            return redirect('login-view')
    return render(request,"signup.html",context)    

class UserDetailView(LoginRequiredMixin,DetailView):
    model=User
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['user']=self.request.user
        return context
@login_required        
def UserUpdateView(request,id):
    if(request.user.id!=id):
        return HttpResponseForbidden()
    if(request.method=="POST"):  
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateform(request.POST,request.FILES,instance=request.user.profile)
        if(u_form.is_valid() and p_form.is_valid()):
            u_form.save()
            p_form.save()
            messages.success(request,f"Profile updated successfuly for User {u_form.cleaned_data['username']}")
            return redirect('user-detail-view',pk=id)
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateform(instance=request.user.profile)    
    context={
        'uform':u_form,
        'pform':p_form
    }
    return render(request,"userupdate.html",context)      