from django.urls import path

from . import views

app_name = 'year_book'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blog_details/<slug:slug>', views.blog_details, name='blog_details', ),
    path('student_details/<slug:slug>', views.student_details, name='student_details'),
    path('students/', views.students, name='students'),
]
