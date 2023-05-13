from django.db import models



# Create your models here.
class Books(models.Model):
    # eid=models.CharField(max_length=120,unique=True,primary_key=True)
    book_name = models.CharField(max_length=120, unique=True)
    author = models.CharField(max_length=80, unique=True)
    amount = models.PositiveIntegerField()
    copies = models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.book_name

    @property
    def m_reviews(self):
        return self.reviews.all()


