from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from Book_store.Form import LoginForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django. contrib.auth.forms import UserCreationForm
from django. contrib. auth.decorators import login_required
from django. contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from Book_store.models import Books,IssueBook
from django.utils import timezone
from django.db.models import Sum
# Create your views here.

def register(request):
	if request.method=="POST":
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("login")
	else:
		form=UserCreationForm()
		return render (request,"Book_store/signup.html",{"form":form})

def Login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            print(user)
            if user is not None:
                login(request,user)
                return redirect('bookview')
            else:
                return HttpResponseRedirect(reverse('login'))
    else:
        form=LoginForm()
        return render(request,'Book_store/signin.html',{'form':form})

@login_required
def BookView(request):
    obj=Books.objects.filter(available=True)
    return render(request,'Book_store/bookview.html',{'obj':obj,'nob':no_of_books})

@login_required
def Issue_Book_to_user(request,id):
    b=Books.objects.get(id=id,available=True)
    IssueBook.objects.create(user=request.user,book=b,issue_date=timezone.now())
    b.available=False
    b.save()
    return HttpResponseRedirect(reverse('bookview'))

def MyBooks(request):
	obj = IssueBook.objects.filter(user=request.user)
	total_fine=0
	for x in obj:
		if x.returned==True:
			total_fine=x.fined+ total_fine
			y=Books.objects.get(id=x.book.id)
			y.available=True
			y.save()
	return render(request,'Book_store/mybooks.html',{'obj':obj,'total_fine':total_fine})
