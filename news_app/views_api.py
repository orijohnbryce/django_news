from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Post
from .serializers import PostSerializer

@api_view(["GET", "POST", "PUT"])
def serve_posts(req):
    """ this is doc """

    if req.method == "GET":
        post_id = req.query_params.get("post_id")
        post = Post.objects.get(pk=post_id)
        ps = PostSerializer(post)
        return Response(ps.data)
    elif req.method == "POST":
        ps = PostSerializer(data=req.data)
        if ps.is_valid():
            ps.save()
            return Response("Object Created")  # temporary
        else:
            return Response({"Error": ps.errors})
    else:
        # update
        post_id = req.query_params.get("post_id")
        post_instance = Post.objects.get(pk=post_id)
        ps = PostSerializer(data=req.data, instance=post_instance)
        if ps.is_valid():
            ps.save()
            return Response("Object updated")  # temporary
        else:
            return Response({"Error": ps.errors}, status=400)
