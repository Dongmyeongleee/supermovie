from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Board, BoardComment
from django.http import JsonResponse
from .serializers import BoardSerializer, BoardListSerializer, BoardCommentSerializer


@api_view(['GET', 'POST',])
def board_list_or_create(request):
    
    def board_list():
        boards = Board.objects.all()
        serializer = BoardListSerializer(boards, many=True)
        return Response(serializer.data)

    def create_board():
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return board_list()
    elif request.method == 'POST':
        return create_board()

@api_view(['GET', 'PUT', 'DELETE'])
def board_detail_or_update_or_delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)

    def board_detail():
        serializer = BoardSerializer(board)
        return Response(serializer.data)

    def update_board():
        serializer = BoardSerializer(instance=board, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete_board():
        if request.user == board.user:
            board.delete()
            return Response(data='delete successfully', status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({'message':'게시글을 작성한 유저만 삭제할 수 있습니다.', 'success': False })

    if request.method == 'GET':
        return board_detail()
    elif request.method == 'PUT':
        return update_board()
    elif request.method == 'DELETE':
        return delete_board()


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def board_comment_list_or_create(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    print('hello')
    if request.method=='GET':
        comments = board.comments.all()
        serializer= BoardCommentSerializer(comments, many=True)
        return Response(serializer.data)
    else:
        serializer = BoardCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, board=board)
            return Response(serializer.data)

@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def board_comment_delete(request, board_comment_pk):
    comment = get_object_or_404(BoardComment, pk=board_comment_pk)
    comment.delete()
    return Response({'id': board_comment_pk})