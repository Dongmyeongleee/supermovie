
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from django.shortcuts import  get_object_or_404
from .models import Movie, Review, UserRank
from django.contrib.auth import get_user_model
from django.http import JsonResponse

from django.conf import settings
from .serializers import  MovieSerializer, ReviewListSerializer, ReviewSerializer, SearchSerializer
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.
@api_view(['GET'])
def movies(request):
    movie_list = get_object_or_404(Movie)
    serializer = MovieSerializer(movie_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def reviews(request, movie_pk):
    review_list = Review.objects.all().filter(movie_id=movie_pk)
    serializer = ReviewListSerializer(review_list, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    UserRank.objects.create(user=request.user, movie=movie,rank =request.data['rank'])
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data)



@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'PUT':
        if review.user == request.user:
            userrank = review.user.userrank_set.filter(user=review.user, movie=review.movie)[0]
            userrank.rank =request.data['rank']
            userrank.save()
            serializer = ReviewSerializer(instance=review,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)


    if request.method == 'DELETE':
        if request.user == review.user:
            review.delete()
            UserRank.objects.filter(user_id=request.user.id, movie_id=review.movie.id).delete()
            return JsonResponse({'message':'게시글이 삭제되었습니다.', 'success': True })
        else:
            return JsonResponse({'message':'게시글을 작성한 유저만 삭제할 수 있습니다.', 'success': False })



@api_view(['POST'])
def recommend(request):


    # 인기순
    favorite_movies = Movie.objects.all().order_by('-vote_average')[:10]
    favorite_serialize = MovieSerializer(favorite_movies, many=True)


    # 개봉순
    recent_movies = Movie.objects.all().order_by('-release_date')[:10]
    recent_serialize = MovieSerializer(recent_movies, many=True)
    

    #알고리즘 추천
    movie_data = Movie.objects.all()
    temp = []
    for movie in range(len(movie_data)):
        score = movie_data[movie].popularity*0.5 + movie_data[movie].vote_average * 10
        temp.append((score, movie_data[movie]))
        temp2 = sorted(temp, key = lambda x :-x[0])[:10]
    temp3 = []
    for i in range(len(temp2)):
        temp3.append(temp2[i][1].title)

    recom_movies = Movie.objects.filter(
        Q(title=temp3[0]) | Q(title=temp3[1]) | Q(title=temp3[2]) | Q(title=temp3[3]) |
        Q(title=temp3[4]) | Q(title=temp3[5]) | Q(title=temp3[6]) | Q(title=temp3[7]) |
        Q(title=temp3[8]) | Q(title=temp3[9]) 
    )
    recom_serialize = MovieSerializer(recom_movies, many=True)
    return Response([favorite_serialize.data, recent_serialize.data, recom_serialize.data])


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_like(request, movie_pk):
    user = request.user 
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        liked = True
    else:
        movie.like_users.add(user)
        liked =False
    return Response(liked)

@api_view(['GET'])
def like_state(request, movie_pk, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    state = user.like_movies.filter(pk=movie_pk).exists()
 
    return Response(state)

@api_view(['POST'])
def movie_like_users(request, movie_pk):
  users = []
  movies = request.data.get('movies')

  for movie in movies:
    movie = get_object_or_404(Movie, pk=movie)
    serializer = MovieSerializer(movie)

    for user in serializer.data.get('like_users'):
      if user not in users:
        users.append(user)
    
  return Response(users)



@api_view(['post'])
def search(request):
    q = request.data.get('query')
    if q:
        movie = Movie.objects.filter(Q(title__icontains=q) | Q(overview__icontains=q)) 
        if movie:
            serializer = SearchSerializer(movie, many=True)
            return Response(serializer.data)

    return Response({'message': '검색결과가 없습니다.'})
    