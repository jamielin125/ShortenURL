from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .forms import SubmitUrlForm
from .models import ShortenURL

# Create your views here.
def Homeview(request):
    form = SubmitUrlForm(request.POST or None)
    context = {
            "title": "URL Shortener",
            "form": form,
    }

    template = "home.html"

    if form.is_valid():
        new_url = form.cleaned_data.get("url")
        obj, created = ShortenURL.objects.get_or_create(url=new_url)
        context = {
            "object": obj,
            "created": created,
        }
        if created:
            template = "success.html"
        else:
            template = "already-exists.html"
    
    return render(request, template ,context)


def URLRedirectview(request, shortcode=None):
    qs = ShortenURL.objects.filter(shortcode__iexact=shortcode)
    if qs.count() != 1 and not qs.exists():
        raise Http404
    obj = qs.first()

    return HttpResponseRedirect(obj.url)