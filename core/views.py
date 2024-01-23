from django import views
from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from .service import link_service


class Redirect(views.View):
    def get(self, request: HttpRequest, short_url: str):
        link = link_service.find_by_short_url(short_url)
        if link is None:
            return render(request, "core/404.html")
        return redirect(to=link.original_url)


class ListLinks(views.View):
    def get(self, request: HttpRequest):
        links = link_service.find_all()
        return render(request, "core/list_links.html", {"links": links})


class CreateLink(views.View):
    def get(self, request: HttpRequest):
        return render(request, "core/create_link.html")

    def post(self, request: HttpRequest):
        original_url = request.POST["original_url"]
        link_service.save(original_url)
        return redirect(to="core:list_links")


class DeleteLink(views.View):
    def post(self, _: HttpRequest, link_id: int):
        link = link_service.find_one(link_id)
        if link is not None:
            link.delete()
        return redirect(to="core:list_links")
