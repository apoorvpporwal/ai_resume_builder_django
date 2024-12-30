from django.shortcuts import render, redirect
from .forms import ResumeForm
from .models import Resume
import random 

# Create your views here.

 # Simulate AI-based keyword suggestion

# Dummy function to simulate AI keyword suggestions based on job role
def get_ai_keywords(job_role):
    # Simulating a database of keywords related to job roles
    keywords_dict = {
        "Software Engineer": ["Python", "Java", "SQL", "Agile", "Git", "JavaScript", "C++"],
        "Data Scientist": ["Python", "Machine Learning", "Statistics", "Data Analysis", "R", "SQL", "TensorFlow"],
        "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Node.js", "MongoDB", "Express"],
        "Digital Marketer": ["SEO", "Google Analytics", "Content Marketing", "AdWords", "Social Media Marketing"]
    }
    
    return keywords_dict.get(job_role, [])

def create_resume(request):
    if request.method == "POST":
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save()
            # Get AI-based keywords for the provided job role
            suggested_keywords = get_ai_keywords(resume.job_role)
            resume.skills = ', '.join(suggested_keywords)  # Suggest these skills in the resume
            resume.save()  # Save the updated resume
            return redirect('resume_list')
    else:
        form = ResumeForm()
    return render(request, 'resumes/create_resume.html', {'form': form})

def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'resumes/resume_list.html', {'resumes': resumes})
