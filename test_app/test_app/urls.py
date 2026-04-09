"""
██████╗░░█████╗░██╗░░░██╗████████╗███████╗██████╗░
██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔══██╗
██████╔╝██║░░██║██║░░░██║░░░██║░░░█████╗░░██████╔╝
██╔══██╗██║░░██║██║░░░██║░░░██║░░░██╔══╝░░██╔══██╗
██║░░██║╚█████╔╝╚██████╔╝░░░██║░░░███████╗██║░░██║
╚═╝░░╚═╝░╚════╝░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝

"""

from django.contrib import admin
from django.urls import path
import sys
sys.path.append("../app")
from app import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.redir_to_home),
    path("signup", views.sign_up),
    path("signin", views.sign_in),
    
    path("<path:subpath>", views.req),
]
