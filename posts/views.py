# posts/views.py
from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy # new

from .forms import PostForm  # new
from .models import Post

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .models import Document

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


class CreatePostView(CreateView):  # new
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')


def home(request):
    documents = Document.objects.all()
    return render(request, 'home2.html', {'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload.html')