"""Paig view for blog and its features"""
from django.shortcuts import render
from django.views import generic

from .forms import CommentForm
from .models import Post


class PostList(generic.ListView):
    """Display all posts on blog filtered by created last"""
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog-index.html'


class PostDetail(generic.DetailView):
    """Single post view"""
    model = Post
    template_name = 'post_details.html'


# class AddPost(CreateView):
    # model = Post
    # template_name ='blog/add_post.html'
    # fields = '__all__'

# class AddCommentView(generic.CreateView):
    # model = Comment
    # template_name = 'blog/add_comment.html'
    # fields = __all__

def add_post(request):
    """ Add post to blog """
    form = CommentForm()
    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
