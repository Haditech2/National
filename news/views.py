from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import NewsPost, Category

# Create your views here.

class NewsListView(ListView):
    model = NewsPost
    template_name = 'news/news_list.html'
    context_object_name = 'news_posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class NewsByCategoryView(ListView):
    model = NewsPost
    template_name = 'news/news_list.html'
    context_object_name = 'news_posts'
    paginate_by = 10

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return NewsPost.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['current_category'] = self.category
        return context


class NewsDetailView(DetailView):
    model = NewsPost
    template_name = 'news/news_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_posts'] = NewsPost.objects.filter(
            category=self.object.category
        ).exclude(pk=self.object.pk)[:3]
        return context
