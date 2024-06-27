from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Post

# {
#     "user": 1,
#     "description": "A post with files",
#     "files": [
#         {
#             "file": "file1.png"
#         },
#         {
#             "file": "file2.mp4"
#         }
#     ]
# }
class PostCreateView(GenericAPIView):
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


