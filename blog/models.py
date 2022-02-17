from email.mime import image
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils import timezone

class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    category=models.CharField(max_length=50)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateField(blank=True, null=True)
    timeRead=models.IntegerField()
    image=models.ImageField(upload_to='Images', default="")
    content=models.TextField()

    def publish(self):
        self.timeStamp = timezone.now()
        self.save()

    def __str__(self):
        return self.title + " by " + self.author


class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username


