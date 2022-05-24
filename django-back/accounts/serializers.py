from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'password',)

class ProfileSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('followers', 'username')
    followers = UserSerializer(many=True)


    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('like_users', 'title', 'poster_path')
    like_movies = MovieSerializer(many=True)
    followings = UserSerializer(many=True)
    class Meta:
        model = get_user_model()
        fields= ('id','like_movies','user_rank','username','followers','followings') 
