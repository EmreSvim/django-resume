from django.shortcuts import render, redirect, get_object_or_404
from core.models import GeneralSetting, ImageSetting, Skill, Experience, Education, Document


# Create your views here.

def get_general_settings(parameter):
    try:
        obj = GeneralSetting.objects.get(name=parameter).parameter
    except:
        obj = ''

    return obj

def get_image_settings(parameter):
    try:
        obj = ImageSetting.objects.get(name=parameter).file
    except:
        obj = ''

    return obj

def layout(request):
    site_title = get_general_settings('site_title')
    site_keywords = get_general_settings('site_keywords')
    site_description = get_general_settings('site_description')
    home_banner_name = get_general_settings('home_banner_name')
    home_banner_title = get_general_settings('home_banner_title')
    home_banner_description = get_general_settings('home_banner_description')
    about_myself_welcome = get_general_settings('about_myself_welcome')
    about_myself_footer = get_general_settings('about_myself_footer')

    # images
    home_banner_image = get_image_settings('home_banner_image')

    documents = Document.objects.all()

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'about_myself_welcome': about_myself_welcome,
        'about_myself_footer': about_myself_footer,
        'home_banner_image': home_banner_image,
        'documents': documents
    }

    return context

def index(request):

    #skills
    skills = Skill.objects.all().order_by('-percentage')

    # experiences
    experiences = Experience.objects.all()

    # education
    educations = Education.objects.all()


    context = {
        'skills': skills,
        'experiences': experiences,
        'educations': educations,
    }

    return render(request, 'index.html', context=context)

def redirect_urls(request, slug):
    doc = get_object_or_404(Document,slug=slug)
    return redirect(doc.file.url)
