
from django.views.generic import ListView
from .models import posts
# Create your views here.

class HomePage(ListView):
    model = posts
    template_name = 'home.html' 
    context_object_name = 'all_posts_list' 
