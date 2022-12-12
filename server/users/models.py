from datetime import datetime, timedelta

import jwt
from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    refreshToken = models.CharField(max_length=255, unique=True, blank=True)
    createdOn = models.TimeField(auto_now_add=True)

    def getAccessToken(self):
        payload = {
            'id': self.id,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }
        # create a environment variable for secret
        jwt_token = jwt.encode(payload, 'secret', algorithm="HS256")
        return jwt_token

    def getRefreshToken(self):
        payload = {
            'id': self.id,
            'exp': datetime.utcnow() + timedelta(days=7)
        }
        jwt_token = jwt.encode(payload, 'secret', algorithm="HS256")
        self.refreshToken = jwt_token
        self.save()
        return jwt_token

    def getPasswordRefreshToken(self):
        payload = {
            'id': self.id,
            'exp': datetime.utcnow() + timedelta(minutes=15)
        }
        reset_token = jwt.encode(payload, self.password, algorithm="HS256")
        # self.
        return reset_token

    def __str__(self):
        return self.username


class Tokenstable(models.Model):
    userid = models.IntegerField(unique=True, null=False, default=2)
    resetToken = models.TextField()

    # def __str__(self):
    #     return self.userid
