from django.shortcuts import render


def check_status():
    if status in range(500, 600):
        return status


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def handler500(request, exception):
    """ Error Handler 500 - Server Error """
    return render(request, "errors/404.html", check_status())
