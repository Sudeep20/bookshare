from django.shortcuts import render,redirect
from .forms import PostForm
from django.utils import timezone

from .models import Document
from .forms import DocumentForm


# Create your views here.
def home(request):
    return render(request, 'profiles/home.html')


def exchange_new(request):

    if request.method == "POST":
        form = PostForm(data=request.POST)
        userform=DocumentForm(request.POST, request.FILES)
        if form.is_valid() and userform.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            userform.save()
            return redirect('home')
    else:
        userform=DocumentForm()
        form = PostForm()
    return render(request, 'exchange/exchange.html', {'form': form,'userform':userform})
