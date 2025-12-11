from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Event

# Create your views here.

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upcoming_events'] = Event.objects.filter(date__gte=timezone.now())
        context['past_events'] = Event.objects.filter(date__lt=timezone.now())
        return context


class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'
