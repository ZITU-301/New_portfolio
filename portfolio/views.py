from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import (
    Profile,
    SocialLink,
    Skill,
    Service,
    Project,
    Education,
    Experience,
    Achievement,
    BlogPost,
    Testimonial,
    ContactMessage,
)


def home(request):
    profile = Profile.objects.first()

    social_links = SocialLink.objects.filter(
        is_active=True
    )

    skills = Skill.objects.all()

    services = Service.objects.filter(
        is_active=True
    )

    projects = Project.objects.filter(
        featured=True
    )[:6]

    education = Education.objects.all()

    experiences = Experience.objects.all()

    achievements = Achievement.objects.all()[:6]

    testimonials = Testimonial.objects.filter(
        is_active=True
    )

    blog_posts = BlogPost.objects.filter(
        published=True
    )[:3]

    context = {
        "profile": profile,
        "social_links": social_links,
        "skills": skills,
        "services": services,
        "projects": projects,
        "education": education,
        "experiences": experiences,
        "achievements": achievements,
        "testimonials": testimonials,
        "blog_posts": blog_posts,
    }

    return render(
        request,
        "portfolio/home.html",
        context
    )


def project_detail(request, slug):
    project = get_object_or_404(
        Project,
        slug=slug
    )

    return render(
        request,
        "portfolio/project_detail.html",
        {
            "project": project
        }
    )


def blog_detail(request, slug):
    blog = get_object_or_404(
        BlogPost,
        slug=slug,
        published=True
    )

    return render(
        request,
        "portfolio/blog_detail.html",
        {
            "blog": blog
        }
    )


def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if name and email and subject and message:

            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )

            messages.success(
                request,
                "Your message has been sent successfully!"
            )

        else:

            messages.error(
                request,
                "Please fill in all fields."
            )

    return redirect("portfolio:home")