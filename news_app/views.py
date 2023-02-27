from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.views.generic import CreateView, UpdateView
from .models import Post


class PostCreation(CreateView):
    model = Post
    fields = "__all__"


@permission_required(["news_app.view_post"], login_url="temp2")
def home(request):
    posts = Post.objects.all()
    return render(request=request, template_name="index.html",
                  context={"posts": posts})


@permission_required("news_app.add_post")
def create_post(req):
    if req.method == "GET":
        # return render
        pass

def create_user(req):

    if req.method.lower() == "get":
        return render(request=req, template_name="signup.html",
                        context={"form": UserCreationForm})

    elif req.method.lower() == "post":
        user_form = UserCreationForm(data=req.POST)

        if user_form.is_valid() :
            user = user_form.save()
            login(request=req, user=user)
            return redirect("home")
        else:
            return render(request=req, template_name="signup.html",
                          context={"form": UserCreationForm})


def edit_post(req):
    return HttpResponse("not impolemetned")


def temp(req):
    return HttpResponse("Connected")

def temp2(req):
    return HttpResponse("you dont' have permissions")


@permission_required("news_app.delete_post")
def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return HttpResponse("Post deleted")


