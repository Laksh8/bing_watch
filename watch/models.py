from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profileimage/',blank=True,null=True)
    profile_discreption = models.TextField(blank=True,null=True)

    def __str__(self):
        return str(self.user)


class Videos(models.Model):
    title = models.CharField(max_length=50)
    discreption = models.CharField(max_length=500,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='thumbnail/',null=True)
    video = models.FileField(upload_to='videos/',)
    likes = models.ForeignKey(User,on_delete=models.CASCADE ,related_name='Likes',null=True,blank=True)
    time = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']



class Comments(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=500)
    video = models.ForeignKey(Videos,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.video)

    class Meta:
       ordering = ['-time']


class CommentLike(models.Model):
    comment = models.ForeignKey(Comments,on_delete=models.CASCADE)
    like = models.ForeignKey(User,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.comment)

    class Meta:
       ordering = ['-time']

class Category(models.Model):
    title = models.CharField(max_length=50)
    video = models.ForeignKey(Videos,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

class Reply(models.Model):
    reply = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reply

    class Meta:
       ordering = ['-time']
