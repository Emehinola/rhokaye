from django.shortcuts import render

# Create your views here.
def access(request):
    return render(request, 'Profile/access.html')

def profile(request):
    return render(request, 'Profile/profile.html')