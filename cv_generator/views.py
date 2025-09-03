from django.shortcuts import render
from .models import ResumeDetailsModel
import logging

logger = logging.getLogger(__name__)

# Create your views here.


def index(request):
    print(request, "REQ")
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone_number = request.POST.get("phone-number", "")
        summary = request.POST.get("summary", "")
        degree = request.POST.get("degree", "")
        school = request.POST.get("school", "")
        university = request.POST.get("university", "")
        previous_work = request.POST.get("previous_work", "")
        skills = request.POST.get("skills", "")

        try:

            profile = ResumeDetailsModel(
                name=name,
                email=email,
                phone_number=phone_number,
                summary=summary,
                degree=degree,
                school=school,
                university=university,
                previous_work=previous_work,
                skills=skills
            )
            profile.save()

        
        except Exception as e:
            logger.error(f"Error occurred while creating resume data: {e}")



        print(request.POST, "POST")
    return render(request=request, template_name='cv_generator/accept.html', context={})