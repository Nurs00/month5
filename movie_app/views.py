from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewSerializer
from rest_framework import status

class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'

# @api_view(['GET', 'PUT', 'DELETE'])
# def director_detail_api_view(request, id):
#     queryset = get_object_or_404(Director, id=id)
#     if request.method == 'GET':
#         serializer = DirectorSerializer(queryset, many=False)
#         return Response(serializer.data, status=200)
#
#     elif request.method == 'PUT':
#         serializer = DirectorSerializer(queryset, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=200)
#     elif request.method == 'DELETE':
#         queryset.delete()
#         return Response(status=204)

class DirectorListCreateAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = PageNumberPagination
# @api_view(['GET'])
# def director_list_api_view(request):
#     if request.method == 'GET':
#         director = Director.objects.all()
#         data = DirectorSerializer(director, many=True).data
#         return Response(data=data)
#
#     elif request.method == 'POST':
#         serializer = DirectorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=200)

class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail_api_view(request, id):
#     queryset = get_object_or_404(Movie, id=id)
#     if request.method == 'GET':
#         serializer = MovieSerializer(queryset, many=False)
#         return Response(serializer.data, status=200)
#
#     elif request.method == 'PUT':
#         serializer = MovieSerializer(queryset, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=200)
#     elif request.method == 'DELETE':
#         queryset.delete()
#         return Response(status=204)

class MovieListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
# @api_view(['GET'])
# def movie_list_api_view(request):
#     if request.method == 'GET':
#         movie = Movie.objects.all()
#         data = MovieSerializer(movie, many=True).data
#         return Response(data=data)
#
#     elif request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=200)


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'
# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail_api_view(request, id):
#     queryset = get_object_or_404(Review, id=id)
#     if request.method == 'GET':
#         serializer = ReviewSerializer(queryset, many=False)
#         return Response(serializer.data, status=200)
#
#     elif request.method == 'PUT':
#         serializer = ReviewSerializer(queryset, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=200)
#     elif request.method == 'DELETE':
#         queryset.delete()
#         return Response(status=204)

class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
# @api_view(['GET'])
# def review_list_api_view(request):
#     if request.method == 'GET':
#         review = Review.objects.all()
#         data = ReviewSerializer(review, many=True).data
#         return Response(data=data)
#
#     elif request.method == 'POST':
#         serializer = ReviewSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=200)

@api_view(['GET'])
def review_stars_api_view(request):
    if request.method == 'GET':
        stars = Movie.objects.all()
        data = MovieReviewSerializer(stars, many=True).data
        return Response(data=data, status=200)