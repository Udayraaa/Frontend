from django.shortcuts import render
from core.settings import EMAIL_HOST_USER
from django.db import connection
from django.template.loader import render_to_string
from django.db import IntegrityError

from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

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

def NevTest(request):
    return render(request, "website/NevTest.html")

def execute_sql(request):
    results = []

    if request.method == "POST":
        sql_query = request.POST.get('sql_query')
        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            results = cursor.fetchall()

    return render(request, 'website/NevTest.html', {'results': results})

# Contact Form Function
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "THIS IS A CONTACT EMAIL"
            email_from = form.cleaned_data["email_from"]

            # Render the HTML content using the new template and form data
            html_message = render_to_string(
                "website/contact.html",
                {
                    "first_name": form.cleaned_data["first_name"],
                    "last_name": form.cleaned_data["last_name"],
                    "email_from": form.cleaned_data["email_from"],
                    "phone_number": form.cleaned_data["phone_number"],
                    "message": form.cleaned_data["message"],
                    # Add other fields as needed
                    # ...
                },
            )

            try:
                send_mail(subject, "", EMAIL_HOST_USER, ["thisisnotaturtle@gmail.com"], html_message=html_message)
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("/")

    form = ContactForm()
    return render(request, "website/contact.html", {"form": form})
      
def success(request):
    return render(request, "sendemail/success.html")