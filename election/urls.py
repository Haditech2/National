from django.urls import path
from . import views

app_name = 'election'

urlpatterns = [
    path('', views.ElectionInfoView.as_view(), name='election_info'),
    path('candidates/', views.CandidateListView.as_view(), name='candidate_list'),
    path('candidate/<int:pk>/', views.CandidateDetailView.as_view(), name='candidate_detail'),
]
