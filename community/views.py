
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'community/index.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'community/detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('community:detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'community/new.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('community:detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'community/edit.html', {'form': form, 'post': post})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('community:index')
