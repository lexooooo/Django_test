import os

BASE_URL = "http://localhost:3001/"

def page_path(page: str):
    
    if not page.endswith(".html"):
        page = page + ".html"
        return os.path.join("html_content", page)

    return os.path.join("html_content", page)
