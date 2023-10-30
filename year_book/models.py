from django.db import models

from django.contrib.auth.models import User

from django.conf import settings

from django.urls import reverse

from datetime import datetime 

from tabnanny import verbose

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user_name
    
class About(models.Model):
    image = models.FileField(blank=False, null=False, upload_to='about')
    name = models.CharField(max_length=100)
    post = models.CharField(max_length=100, help_text="Designation of the member eg CEO")
    short_description = models.TextField()
    time_uploaded = models.DateTimeField('date uploaded', default=datetime.now())
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def about_img(self):
        if self.user_image:
          return self.image.url
    
    class Meta():
        verbose_name_plural = 'About'


class Blog(models.Model):
    blog_title = models.CharField(max_length=250)
    blog_image = models.FileField(blank=False, null=False, upload_to='blog')
    blog_post = models.TextField()
    post_writer = models.CharField(max_length=200, default='Anon')
    category = models.CharField(max_length=20, default="Culture")
    slug = models.SlugField(max_length=250, unique=True)
    time_uploaded = models.DateTimeField('date uploaded', default=datetime.now())
    approve = models.BooleanField(default=False)
    
    def get_blog_title(self):
        if self.blog_title:
            return self.blog_title
    
    def get_blog_image(self):
        if self.blog_image:
            return self.blog_image.url
    
    def get_blog_post(self):
        if self.blog_post:
            return self.blog_post
    
    def get_blog_writer(self):
        if self.post_writer:
            return self.post_writer
    
    def get_blog_cat(self):
        if self.category:
            return self.category
    
    def get_date(self):
        if self.time_uploaded:
            return self.time_uploaded
    
    def get_blog_url(self):
        return reverse('year_book:blog_details', kwargs={'slug':self.slug} )
    
    def __str__(self) -> str:
        return f"{self.blog_title}"
    
    class Meta():
        verbose_name_plural = 'Blog'

class Comment(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=150, verbose_name= 'User Name')
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_content = models.TextField(verbose_name= 'Content')
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name


class Contact_Us(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=50, default='complaint')
    email = models.EmailField(max_length=50)
    message = models.TextField()
    created =models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta():
        verbose_name_plural = 'Contact Us'
        
    def __str__(self) -> str:
        return f"{self.email}"
    
class Year_Book(models.Model):
    student_first_name = models.CharField(max_length=200, blank=False)
    student_last_name = models.CharField(max_length=200, blank=False)
    student_nick_name = models.CharField(max_length=100, blank=False)
    student_image = models.FileField(blank=False, null=False, upload_to='student')
    email = models.EmailField(blank=False)
    phone_number = models.CharField(max_length=11, blank=False)
    favorite_course = models.CharField(max_length=100, blank=False)
    favorite_lecturer = models.CharField(max_length=100, blank=False)
    most_challenging_course = models.CharField(max_length=100, blank=False)
    relationship_status = models.CharField(max_length=100)
    date_of_birth = models.DateField(auto_now_add=True)
    hobbies = models.CharField(max_length=200)
    fun_fact_about_me = models.TextField()
    favorite_quote = models.TextField()
    resident_address = models.CharField(max_length=500)
    twitter_handle = models.URLField(max_length=200, blank=True)
    facebook_handle = models.URLField(max_length=200, blank=True)
    github = models.URLField(max_length=200, blank=True)
    linkedin = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    time_uploaded = models.DateTimeField('date uploaded', default=datetime.now())
    approve = models.BooleanField(default=False)
    

    class Meta():
        verbose_name_plural = 'Class Year Book'
        
    def __str__(self) -> str:
        return f"{self.email}"
    
     
    def get_student_url(self):
        return reverse('year_book:student_details', kwargs={'slug':self.slug} )
    
    


