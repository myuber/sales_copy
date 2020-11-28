from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=50)
    posted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Copy(models.Model):
    text = models.CharField(max_length=100)
    posted_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(to=Article, related_name="sales_copy", on_delete=models.CASCADE)
    def __str__(self):
        return self.sales_copy 