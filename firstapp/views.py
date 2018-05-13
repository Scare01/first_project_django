from django.shortcuts import render
from datetime import datetime

def index(request):
    today = datetime.now().date()
    return render(request, "/Users/aleksei/Documents/work/django_projects/firstproject/firstapp/templates/index.html",
                     {"today": today})




