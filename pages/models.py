from django.db import models

class Page(models.Model):
    TYPE_CHOICES = (
        ('tutorial', 'Tutorial'),
        ('video', 'Video'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='tutorial')
    content = models.CharField(max_length=254)
    video = models.URLField()


    def __str__(self):
        return self.content

class Tutorial(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='tutorials', null=True)
    content = models.TextField()

class Video(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='videos', null=True)
    video = models.URLField()
