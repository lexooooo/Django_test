from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import Users
from django.templatetags.static import static
from django.shortcuts import render
from django.template.loader import render_to_string
import sys
import os
import logging
import json
from var import var
logger = logging.getLogger("django")


### CREATE PATHS TO STATIC FILES !!!   TODO !!!!
sys.stdout = open(r"C:\Users\lexok\Desktop\django\test_app\django.log", "a")

def req(request, subpath):
    
    if subpath == "user":
        if request.user.is_authenticated:
            return HttpResponse("<h1>AUTHORIZED</h1>")
        else:
            return HttpResponse("<h1>AUTHORIZATION NEEDED</h1>")
    
    content = "<h1>DJANGO APP SERVER --------- path is %s ---------</h1>" % subpath
    
    current_page = "page.html"
    cont = render_to_string(os.path.join("html_content", current_page), {"TEXT": "CONTEXT TEXT FOR CHILD HTMLPAGE"})
    # logger.info(f"========================{request.path}")
    return render(request, "index.html", context={"content": cont})
    
    # res = HttpResponse(content)
    # logger.info(request.path)
    
    # if subpath == "user":
    #     file_path = static("index.html")
    #     return render(request, "index.html", context={"content": "USER"})
    # return res



def redir_to_home(request):
    response = HttpResponseRedirect("/home")
    response.status_code = 302
    return response

def sign_up(request):
    if request.method == "POST":
        credentials = json.loads(request.body)
        
        try:
            user = Users.objects.create(**credentials)
            user.save()
            logger.info("USER -{}- HAS SIGNED UP".format(credentials["username"]))
        except Exception as err:
            if err.args[0] == 1062:
                logger.error("============={}".format("USER ALREADY EXISTS !!!"))
                return HttpResponse("USER ALREADY EXISTS !!!") 
            logger.error("============={}".format(err))
            raise err
        
        response = HttpResponse("POST REQUEST RECIEVED")
        response["Content-Type"] = "text/plain"
        return response
    else:
        # logger.info("WRONT METHOD")
        # ### IF METHOD IS GET, REDIRECT TO HOME PAGE
        # return redir_to_home(request)
        content = render_to_string(
            var.page_path("signup.html"), 
            context={"action": var.BASE_URL+"signup"}
            )
        # logger.info(content)
        
        return render(request, "index.html", context={"content": content})

def sign_in(request):
    if request.method == "POST" and request.path == "signin":
        credentials = json.loads(request.body.decode("utf-8"))
        username = credentials.get("username")
        password = credentials.get("password")
        
        try:
            auth = authenticate(request, credentials)
            if auth is not None:
                login(request, auth)
                return HttpResponse("<h1>LOGGED IN</h1>")
        except Exception as err:
            raise err
    else:
        response = HttpResponse()
        response.status_code = 404
        return response