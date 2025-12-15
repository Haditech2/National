from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Executive
from news.models import NewsPost
from events.models import Event
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
@require_http_methods(["GET", "POST"])
def setup_admin(request):
    """One-time admin setup view - DELETE THIS AFTER USE"""
    secret_key = request.GET.get('key') or request.POST.get('key')
    if secret_key != 'naas2025setup':
        return HttpResponse('Access denied', status=403)
    
    username = 'admin'
    email = 'admin@naas.org'
    password = 'NaasAdmin2025!'
    
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        msg = f'Password updated for "{username}"'
    else:
        User.objects.create_superuser(username=username, email=email, password=password)
        msg = f'Superuser "{username}" created successfully'
    
    return HttpResponse(f'''
        <h2>{msg}</h2>
        <h3>Admin Login Details:</h3>
        <p><strong>URL:</strong> <a href="/admin/">/admin/</a></p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Password:</strong> {password}</p>
        <br>
        <p style="color: red;"><strong>IMPORTANT:</strong> Change your password after login and delete the setup_admin view!</p>
    ''')
