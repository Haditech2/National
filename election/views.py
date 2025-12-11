from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Candidate

# Create your views here.

class ElectionInfoView(TemplateView):
    template_name = 'election/election_info.html'


class CandidateListView(ListView):
    model = Candidate
    template_name = 'election/candidate_list.html'
    context_object_name = 'candidates'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        positions = Candidate.objects.values_list('position', flat=True).distinct()
        context['positions'] = positions
        context['candidates_by_position'] = {
            pos: Candidate.objects.filter(position=pos) for pos in positions
        }
        return context


class CandidateDetailView(DetailView):
    model = Candidate
    template_name = 'election/candidate_detail.html'
    context_object_name = 'candidate'
