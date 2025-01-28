from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Algorithm(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    complexity_time = models.CharField(max_length=50, blank=True, null=True)
    complexity_space = models.CharField(max_length=50, blank=True, null=True)
    input_example = models.TextField(blank=True, null=True)
    output_example = models.TextField(blank=True, null=True)
    pseudocode = models.TextField(blank=True, null=True)
    implementation = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name='algorithms')

    def __str__(self):
        return self.name
