from django.urls import path

from . import views

app_name = "store"

urlpatterns = [
path("", views.home_page, name="homePage"),
path("about/", views.about, name="aboutPage"),
path("services/", views.services, name="servicesPage"),
path("resources/", views.resources, name="resourcesPage"),
path("contact/", views.contact, name="contactPage"),
path("blogSummary/", views.blog_summary, name="blogSummaryPage"),
path('NevTest/', views.execute_sql, name='execute_sql'),

]