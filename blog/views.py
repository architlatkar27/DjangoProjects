from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
from blog.models import BlogPost, Like
from blog.forms import CreateBlogPostForm, UpdateBlogPostForm
from account.models import Account
from django.db.models import Q
import inspect
# Create your views here.
def create_blog_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    
    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        form = CreateBlogPostForm()
    context['form'] = form

    return render(request,'blog/create_blog.html',context)

def detail_blog_view(request,slug):
    context = {}
    blog_post = get_object_or_404(BlogPost,slug=slug)
    context["blog_post"] = blog_post
    if request.user != blog_post.author and str(inspect.stack()[2][3])!="like_post_view":
        blog_post.views+=1
    blog_post.save()
    return render(request,'blog/detail_blog.html',context)

def edit_blog_view(request,slug):
    context = {}
    if not request.user.is_authenticated:
        return redirect('must_authenticate')

    blog_post = get_object_or_404(BlogPost,slug=slug)
    if blog_post.author != request.user:
        return HttpResponse("You are not the author for this post")
    if request.POST:
        form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context["success_message"] = "Blog Updated!"
            blog_post = obj

    form = UpdateBlogPostForm(
        initial={
            'title' : blog_post.title,
            'body' : blog_post.body,
            'image' : blog_post.image,
        }
    )
    context["update_form"] = form
    return render(request,'blog/edit_blog.html',context)

def like_post_view(request,slug):
    if not request.user.is_authenticated:
        return redirect('must_authenticate')
    post = get_object_or_404(BlogPost,slug=slug)
    if request.user == post.author:
        return HttpResponse("Don't try to be cheeky. You cannot like your own post")

    new_like, created = Like.objects.get_or_create(user=request.user,post=post)
    if not created:
        return detail_blog_view(request,slug)
    else:
        post.likes+=1
        post.save()
        return detail_blog_view(request,slug)