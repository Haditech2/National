from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Executive
from news.models import NewsPost
from events.models import Event
from django.utils import timezone

# Create your views here.

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_news'] = NewsPost.objects.filter(featured=True)[:3]
        context['latest_news'] = NewsPost.objects.all()[:4]
        context['upcoming_events'] = Event.objects.filter(date__gte=timezone.now())[:3]
        context['executives'] = Executive.objects.all()[:6]
        return context


class AboutView(TemplateView):
    template_name = 'core/about.html'


class ContactView(TemplateView):
    template_name = 'core/contact.html'


class ExecutivesView(ListView):
    model = Executive
    template_name = 'core/executives.html'
    context_object_name = 'executives'
