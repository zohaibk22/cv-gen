from django.shortcuts import render

# Create your views here.


def index(request):
    print(request, "REQ")
    return render(request=request, template_name='cv_generator/accept.html', context={})