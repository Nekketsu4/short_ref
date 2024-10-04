from django.shortcuts import render

from app.models import URL
from app.forms import CreateShortURLForm


def index(request):
    return render(request, 'index.html')

def create_short_url(request):
    if request.method == 'POST':
        form = CreateShortURLForm(request.POST)
        if form.is_valid():
            form.save()
        url = URL.objects.last()
        form = CreateShortURLForm()
        return render(
            request,
            'get_short_url.html',
            {'url': url, 'form': form}
        )
    form = CreateShortURLForm()
    return render(
        request,
        'get_short_url.html',
        {'form': form}
    )


def list_short_urls(request):
    urls = URL.objects.all()
    return render(
        request,
        'list_urls.html',
        {'urls': urls}
    )
