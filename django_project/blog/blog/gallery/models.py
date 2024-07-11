from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def edit(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image
        self.save()

    def short_description(self):
        # Split the description into words
        words = self.description.split()
        if len(words) > 50:
            # Join the first 50 words and add "..." at the end
            return ' '.join(words[:30]) + '...'
        else:
            # If the description is already less than 50 words, return it as is
            return self.descriptio
