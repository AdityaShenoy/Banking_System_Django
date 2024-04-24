from django.shortcuts import render
from django.urls import reverse
from django.http import HttpRequest
from django.forms import Form


def render_form(request: HttpRequest, title: str, url_name: str, form: Form):
    return render(
        request, "forms.html", {"title": title, "url": reverse(url_name), "form": form}
    )
