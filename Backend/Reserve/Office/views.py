from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# old version
# def home_page(request):
#     return render(request, "Office/test.html", {})


# new version
class HomePageView(TemplateView):
    template_name = 'Office/test.html'