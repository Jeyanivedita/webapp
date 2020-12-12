from django.shortcuts import render, redirect
from blog.forms import PostForm
from blog.models import Post


def home(request):
    post = Post.objects.all()

    data = {
        'posts': post
    }

    return render(request, template_name='blog/home.html', context=data)


def about(request):
    return render(request, template_name='blog/about.html')


def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-url')

    data = {
        'form': form
    }
<<<<<<< HEAD
    return render(request, template_name='blog/createPost.html', context=data)
=======
    return render(request, template_name='blog/createPost.html', context=data)
>>>>>>> d9a48e455d2e97535714dd5a0d5e18a452cd9bce
