import logging
from django.db.models.query import QuerySet
from django.views import View
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.utils import IntegrityError

from posts.models import Posts,Images
logger = logging.getLogger

class PostView(View):
  def get(self,request:HttpRequest)->HttpResponse:
    posts: Posts=Posts.objects.all()
    if not posts:
      return render(
        request=request,template_name="posts.html",
        status=404,
      )
    return render(
      request=request,
      template_name="posts.html",
      context={"posts": posts}
    )

  def post(self,request:HttpRequest)->HttpResponse:
    pass

  def put(self,request:HttpRequest)->HttpResponse:
    pass

  def patct(self,request:HttpRequest)->HttpResponse:
    pass

  def delett(self,request:HttpRequest)->HttpResponse:
    pass
