from django.shortcuts import render
from .models import About, CollaborateRequest
from .forms import CollaborateForm

# Create your views here.
def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()

    """ return render(
        request,
        "about/about.html",
        {"about": about},
    ) """

    collaboration_form = CollaborateForm()

    context = {"about": about,
               "collaboration_form": collaboration_form
               }
            
    return render(
         request,
        "about/about.html",
        context,
    )