from django.shortcuts import render, get_object_or_404

def home_view(request):
    return render(request,'polls/home.html')