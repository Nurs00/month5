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
class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True)