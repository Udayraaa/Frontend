from django.shortcuts import render

def home_page(request):
    return render(request, "website/index.html")

def about(request):
    return render(request, "website/about.html")

def services(request):
    return render(request, "website/services.html")

def resources(request):
    return render(request, "website/resources.html")

def contact(request):
    return render(request, "website/contact.html")

def blog_summary(request):
    return render(request, "blog/blogSummary.html")