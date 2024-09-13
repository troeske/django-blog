from django.shortcuts import render
from django.contrib import messages
from .models import About, CollaborateRequest
from .forms import CollaborateForm

# Create your views here.
def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()

    if request.method == "POST":
        print("Received a POST request")
        collaboration_form = CollaborateForm(data=request.POST)
        if collaboration_form.is_valid():
            collaboration_form.save()
            """ collaboration.author = request.user
            collaboration.name = 
            collaboration.email =
            collaboration.message =
            collaboration.save() """
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavor to respond within 2 working days.'
                )

    collaboration_form = CollaborateForm()

    context = {"about": about,
               "collaboration_form": collaboration_form
               }
            
    return render(
         request,
        "about/about.html",
        context,
    )