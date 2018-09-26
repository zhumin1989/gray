from rest_framework import serializers
from .models import Quest,Log,Treasure,Sign,Img,User


class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = ('id', 'title', 'reward', 'req_user', 'date', 'content','keyword','flag')


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ('id', 'label', 'catlog', 'date', 'pub_deptment')


class TreasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treasure
        fields = ('id', 'title', 'item', 'value', 'tcreate_date', 'store','stat','flag','img')


class SignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sign
        fields = ('id','date')


class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Img
        fields = ('id', 'title', 'img')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'work_number', 'name','create_datetime','currency','total_currency','quest','treasure',
                  'token','department','is_administer','img')
