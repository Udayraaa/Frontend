from django.shortcuts import render

from django.db import connection

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
