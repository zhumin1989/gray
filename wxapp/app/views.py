from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from .models import User,Log,Treasure,Quest,Sign,Img
from .serializers import  QuestSerializer,SignSerializer,LogSerializer,ImgSerializer,TreasureSerializer,UserSerializer
from rest_framework import mixins
from rest_framework import generics

def index(request):
    return render(request, 'app/index.html', {})


def room(request, room_name):
    return render(request, 'app/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


class QuestList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    List all snippets, or create a new snippet.
    """

    queryset = Quest.objects.all()
    serializer_class = QuestSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    # def get(self, request, format=None):
    #     snippets = Quest.objects.all()
    #     print(snippets)
    #     serializer = QuestSerializer(snippets, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request, format=None):
    #     serializer = QuestSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestDetail(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    # def get_object(self, pk):
    #     try:
    #         return Quest.objects.get(pk=pk)
    #     except Quest.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = QuestSerializer(snippet)
    #     return Response(serializer.data)
    #
    # def put(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = QuestSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class LogList(generics.ListCreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer


class LogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer


class SignList(generics.ListCreateAPIView):
    queryset = Sign.objects.all()
    serializer_class = SignSerializer


class SignDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sign.objects.all()
    serializer_class = SignSerializer


class TreasureList(generics.ListCreateAPIView):
    queryset = Treasure.objects.all()
    serializer_class = TreasureSerializer


class TreasureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Treasure.objects.all()
    serializer_class = TreasureSerializer


class ImgList(generics.ListCreateAPIView):
    queryset = Img.objects.all()
    serializer_class = ImgSerializer


class ImgDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Img.objects.all()
    serializer_class = ImgSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer