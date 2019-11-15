from django.db import models

class Members(models.Model):

    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    photourl = models.CharField(max_length=300)

class Secretaries(Members):
    pass
class Core(Members):
    pass
class Executive(Members):
    pass
class gallery(models.Model):
    picurl = models.CharField(max_length=300)