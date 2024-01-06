from django.urls import path
from .views import about_view,blog_view, contact_view, home_view

urlpatterns = [
    path('about/', about_view),
    path('contact/', contact_view),
    path('blog/', blog_view),
    path('', home_view)
]