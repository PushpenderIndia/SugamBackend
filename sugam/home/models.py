from django.db import models

class DocSummarized(models.Model):
    original_txt = models.TextField()
    summarized_txt = models.TextField()

    def __str__(self):
        return self.original_txt[:50]  # Display a truncated version of the original text in the admin interface

class ComikifyModel(models.Model):
    topic = models.CharField(max_length=255)
    result = models.JSONField()

    def __str__(self):
        return self.topic
