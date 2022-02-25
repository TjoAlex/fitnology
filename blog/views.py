"""Paig view for blog and its features"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic

from .forms import PostForm
from .models import Post


class PostList(generic.ListView):
    """Display all posts on blog filtered by created last"""
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog-index.html'


class PostDetail(generic.DetailView):
    """Single post view"""
    model = Post
    template_name = 'post_details.html'


@login_required
def add_post(request):
    """ Add a post to the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can work on posts.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = PostForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


# Edit post
@login_required
def edit_post(request, post_id):
    """ Edit a post in the store blog"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('blog'))

    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated post!')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Failed to update post. Please ensure the form is valid.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


# Delete post
@login_required
def delete_post(request, post_id):
    """ Delete a post from the store blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('blog'))

    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Post Deleted!')
    return redirect(reverse('blog'))
