from django.db import models

class Wpis(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    active = models.BooleanField(default=True)
    #opcjonalne
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Lista wpisów"