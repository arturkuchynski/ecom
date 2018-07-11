from django.shortcuts import render


def not_found_404(request):
    page_title = '404 Page Not Found'
    return render(request, '404.html', locals())


def internal_server_error_500(request):
    page_title = '500 Page Internal Server Error'
    return render(request, '500.html', locals())
