from __future__ import unicode_literals
from ..validation.models import User
from django.db import models
from django.db.models import Count

# Create your models here.
class SecretAction(models.Manager):
    def makeSecret(self, POST_data):
        if POST_data['secret']:
            self.create(secrets=POST_data['secret'],writer=User.objects.get(id=POST_data['user_id']))
        return
    def deleteSecret(self, id):
        self.get(id=id).delete()
        return
    def likeSecret(self, user, msg):
        post = Secret.objects.get(id=msg)
        likedBy = User.objects.get(id=user)
        post.likes.add(likedBy)
        return
    def getSecrets(self):
        return self.annotate(numLikes=Count('likes')).all().order_by('-created_at')
    def getPopular(self):
        return self.annotate(numLikes=Count('likes')).all().order_by('-numLikes', '-created_at')[:10]

class Secret(models.Model):
    secrets = models.CharField(max_length=120)
    writer  = models.ForeignKey(User, related_name='user_secrets')
    likes = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = SecretAction()
