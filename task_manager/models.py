from django.db import models
from django.urls import reverse

class my_class(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    text = models.TextField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('task_manager:task_manager_detail', kwargs={'slug': self.slug})
