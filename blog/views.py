"""Paig view for blog and its features"""
from django.shortcuts import render, redirect, reverse
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


# class AddCommentView(generic.CreateView):
    # model = Comment
    # template_name = 'blog/add_comment.html'
    # fields = __all__


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


# Edit Post
def edit_post(request, id):
    if not request.user.is_superuser:
        return render(request, 'blog/edit_post.html')
    else:
        return redirect(reverse('blog'))


# Delete Post
def delete_post(request, id):
    if not request.user.is_superuser:
        return render(request, 'blog/delete_post.html')
    else:
        return redirect(reverse('blog'))
