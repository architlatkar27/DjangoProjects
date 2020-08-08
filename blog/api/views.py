from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from account.models import Account
from blog.models import BlogPost
from blog.api.serializers import BlogPostSerializer

#API DETAIL VIEW
@api_view(['GET', ])
@permission_classes((IsAuthenticated))
def api_blog_detail_view(request,slug):
    try:
        blogpost = BlogPost.objects.get(slug=slug)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BlogPostSerializer(blogpost)
    return Response(serializer.data)

#API UPDATE VIEW
@api_view(["PUT",])
@permission_classes((IsAuthenticated))
def api_blog_update_view(request,slug):
    try:
        blogpost = BlogPost.objects.get(slug=slug)
    except:
        return Response(status = status.HTTP_404_NOT_FOUND)
    user = request.user
    if blogpost.author != user:
        return Response({'response':'you donot have permission to edit this post'})
    data = {}
    serializer = BlogPostSerializer(blogpost)
    if request.method=="PUT":
        if serializer.is_valid():
            serializer.save()
            data["success"] = "your update was successful:)"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#API DELETE VIEW
@api_view(['DELETE',])
@permission_classes((IsAuthenticated))
def api_blog_delete_view(request,slug):
    try:
        blogpost = BlogPost.objects.get(slug=slug)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    user = request.user
    if blogpost.author != user:
        return Response({'response':'you donot have permission to edit this post'})
    data = {}
    operation = blogpost.delete()
    if operation :
        data["success"] = "deletion was successful:)"
    else :
        data["failure"] = "deletion was unsuccessful:("
    return Response(data=data)

@api_view(['POST',])
@permission_classes((IsAuthenticated))
def api_blog_create_view(request):
    account = request.user

    blogpost = BlogPost(author=account)
    serializer = BlogPostSerializer(blogpost,data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )

