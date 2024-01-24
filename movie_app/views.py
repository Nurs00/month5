from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewSerializer
from rest_framework import status


@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not Found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializer(director).data
    return Response(data=data)


@api_view(['GET'])
def director_list_api_view(request):
    director = Director.objects.all()

    data = DirectorSerializer(director, many=True).data

    return Response(data=data)

@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not Found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = MovieSerializer(movie).data
    return Response(data=data)


@api_view(['GET'])
def movie_list_api_view(request):
    movie = Movie.objects.all()

    data = MovieSerializer(movie, many=True).data

    return Response(data=data)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not Found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializer(review).data
    return Response(data=data)


@api_view(['GET'])
def review_list_api_view(request):
    review = Review.objects.all()

    data = ReviewSerializer(review, many=True).data

    return Response(data=data)

@api_view(['GET'])
def review_stars_api_view(request):
    stars = Movie.objects.all()

    data = MovieReviewSerializer(stars, many=True).data

    return Response(data=data, status=200)