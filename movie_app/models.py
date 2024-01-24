from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies', null=True, blank=True)

    def __str__(self):
        return self.title

STAR_CHOICES = (
    (i, '*' * i) for i in range(1, 6)
)

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=STAR_CHOICES, default=5)


    def __str__(self):
        return self.movie.title