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

# Update contact function
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Contact Form Inquiry"

            body = {
                'first_name': form.cleaned_data['first_name'], 
                'last_name': form.cleaned_data['last_name'], 
                'email_address': form.cleaned_data['email_from'], 
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message'], 
            }
            message = "\n".join(body.values())

            # Defining table values
            form_first_name = form.cleaned_data['first_name']
            form_last_name = form.cleaned_data['last_name']
            form_email = form.cleaned_data['email_from']
            form_message = form.cleaned_data['message']
            form_subject = form.cleaned_data['subject']


            try:
                send_mail(form_subject, message, EMAIL_HOST_USER, [form_email], html_message=message.replace("\n", "<br>"))
                
                with connection.cursor() as cursor:
                    # Insert data into the database table
                    sql_insert = "INSERT INTO dbo.ContactSubmissions (name, email, subject, message, date) VALUES (%s, %s, %s, %s, GETDATE())"
                    cursor.execute(sql_insert, (f"{form_first_name} {form_last_name}", form_email, form_subject, form_message,))
                
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("/")  # Redirect to the success page upon successful submission

    form = ContactForm()
    return render(request, "website/contact.html", {"form": form})