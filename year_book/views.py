from django.shortcuts import render, get_object_or_404, redirect

from django.core.exceptions import ObjectDoesNotExist

from year_book.models import *

from django.contrib import messages

from django.urls import reverse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.conf import settings 

import json

import requests

# Create your views here.
def home(request):
    students = Year_Book.objects.order_by('-time_uploaded')
    blog = Blog.objects.order_by('-time_uploaded')[:3]
    context = {'student_key':students, 'blog_key':blog}
    return render(request, 'client/index.html', context)

def about(request):
    about = About.objects.order_by('-time_uploaded')
    return render(request, 'client/about.html', {'about':about})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        print(name, email, subject, message)
        
        data = Contact_Us.objects.create(name=name, email=email, subject=subject, message=message)
        
        data.save()
        print('Success')
        messages.success(request, 'Your Message was Delivered Successfully')
        
    return render(request, 'client/contact.html')


def students(request):
    products = Year_Book.objects.order_by('-time_uploaded')
    paginator = Paginator(products, 4)
    page_number = request.GET.get('page', 1)

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)


    return render(request, 'client/students.html',{'products':page_obj})

def student_details(request, slug):
    product = get_object_or_404(Year_Book, slug=slug)
    return render(request, 'client/students_details.html',{'product':product})

def blog(request):
    blog_post = Blog.objects.order_by('-time_uploaded')
    paginator = Paginator(blog_post, 3)
    page_number = request.GET.get('page', 1)

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
   
    return render(request, 'client/news.html', {'post':page_obj})

def blog_details(request, slug):
    blog_details = get_object_or_404(Blog, slug=slug)
    return render(request, 'client/blog-details.html', {'post':blog_details})


