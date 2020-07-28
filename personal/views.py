from django.shortcuts import render
from account.models import Account
from blog.models import BlogPost
# from personal.models import Question
# Create your views here.

def home_screen_view(request):
    context = {}
    context["accounts"] = Account.objects.all()
    all_posts = BlogPost.objects.all()
    context["all_posts"] = all_posts

    return render(request,'personal/home.html',context)