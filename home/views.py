from django.shortcuts import render

# function to render home app


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')