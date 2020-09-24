from django.db import models


class Landmark(models.Model):
    country = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    photo = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    landmark = models.ForeignKey(Landmark, on_delete=models.CASCADE, related_name='comment')
    title = models.CharField(max_length=150)
    contents = models.TextField()

    def __str__(self):
        return self.title
