from django.shortcuts import render
from .models import ResumeDetailsModel
import logging
from django.http import Http404
from django.views.decorators.http import require_http_methods
from django.http import (
    HttpResponse, HttpResponseBadRequest, JsonResponse
)
from django.template import loader
import io
from weasyprint import HTML


logger = logging.getLogger(__name__)

# Create your views here.

@require_http_methods(["GET", "POST"])
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

    return render(request=request, template_name='cv_generator/accept.html', context={})



@require_http_methods(["GET", "POST"])
def generate_cv(request, id):
    try:
        current_resume = ResumeDetailsModel.objects.filter(id=id).first()
        

        if not current_resume:
            raise Http404("Resume not found")
        

        context = {"resume": current_resume}

        template = loader.get_template('cv_generator/resume_template.html')
        html = template.render(context)
        # this takes an html string and convert it to a pdf document using WeasyPrint
        pdf_file = HTML(string=html).write_pdf()
       
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{current_resume.name}_resume.pdf"'
        return response
    except Exception as e:
        logger.error(f"Error occurred while fetching resume data: {e}")
        return HttpResponseBadRequest("Bad Request")
    
