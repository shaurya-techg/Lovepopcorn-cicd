from django.db import models

class Movie(models.Model):
    GENRE_CHOICES = [
        ("Action", "Action"),
        ("Adventure", "Adventure"),
        ("Animation", "Animation"),
        ("Comedy", "Comedy"),
        ("Crime", "Crime"),
        ("Drama", "Drama"),
        ("Fantasy", "Fantasy"),
        ("Horror", "Horror"),
        ("Romance", "Romance"),
        ("Sci-Fi", "Sci-Fi"),
        ("Thriller", "Thriller"),
    ]

    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    release_year = models.PositiveIntegerField()
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField()
    poster_url = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
