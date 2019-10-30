from rest_framework import viewsets
from post.models import Post # 데이터 처리 대상
from post.serializer import PostSerializer #status에 따라 직접 response를 처리
from django.http import Http404 # get object or 404직접 구현
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView # APIView를 상속받은 CBV
from rest_framework.response import Response
from rest_framework import status


#CBV

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True) #쿼리셋 넘기기
        return Response(serializer.data) # 직접 response(serializer, data) 리턴

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(): #직접 유효성 검사
            serializer.save() #저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView): # 얘는 pk값을 받는다.(메소드에 pk인자)

    def get_object(self, pk): #get_object_or_404 구현
        try:
            return Post.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
