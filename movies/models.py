from django.db import models


class Movie(models.Model):
    GENRE_CHOICES = [
        ("Action", "Action"),
        ("Adventure", "Adventure"),
        ("Comedy", "Comedy"),
        ("Drama", "Drama"),
        ("Fantasy", "Fantasy"),
        ("Horror", "Horror"),
        ("Romance", "Romance"),
        ("Sci-Fi", "Sci-Fi"),
        ("Thriller", "Thriller"),
    ]

    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES)
    release_year = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    description = models.TextField()
    poster_url = models.URLField(blank=True)

    def __str__(self):
        return self.title
