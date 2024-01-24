from rest_framework import serializers
from .models import Director, Review, Movie


class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = '__all__'

    def get_movie_count(self, obj):
        return obj.movies.count()

class MovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_average_rating(self, obj):
        total_stars = sum(review.stars for review in obj.reviews.all())
        num_reviews = obj.reviews.count()
        if num_reviews > 0:
            return total_stars / num_reviews
        else:
            return 0.0

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text movie stars'.split()

class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'
