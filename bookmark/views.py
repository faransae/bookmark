from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 4


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'


class BookmarkDetailView(DetailView):
    model = Bookmark



