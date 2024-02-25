from django.db import models

class Thesis(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    abstract = models.TextField()
    year = models.IntegerField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    thesis = models.ForeignKey(Thesis, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.created_at} on {self.thesis}"