from django.http import HttpResponse




class StatusChecker():
    
    def __init__(self, response):
        self.response = response
        
    def __call__(self, request):
        # BEFORE views.py
        
        ### IGNORE REQUEST IF /FAVICON.ICO PATH IS REQUESTED
        if request.path == "/favicon.ico":
            return HttpResponse(status=204)
        
        # AFTER views.py
        response = self.response(request)
        status_code = response.status_code
        
        if status_code == 404 or str(status_code).startswith("50") or request.path == "/error":
            response.content = "<h1 style='color: red;'>SOMETHING WENT WRONG</h1>"
            response["Content-Length"] = len(response.content)
            return response
        
        return response