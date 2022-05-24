from rest_framework import serializers
from .models import Board, BoardComment




class BoardListSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
  
    def get_username(self,obj):
        return obj.user.username
    class Meta: 
        model = Board
        fields = ('id','title','user','username')
        read_only_fields = ('user',)

class BoardSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    def get_username(self,obj):
        return obj.user.username
    # created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    # updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    class Meta: 
        model = Board
        fields = ('id','title', 'username','content', 'user',)
        read_only_fields = ('user','username',)

class BoardCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardComment
        fields = ('id','user', 'board', 'content', 'created_at', 'updated_at')
        read_only_fields = ('user', 'board', 'created_at', 'updated_at')