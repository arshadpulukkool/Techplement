from django.contrib.auth.models import User
from django.db import models


# History model is used for saving calculations history of logged in users
class History(models.Model):
    value1 = models.CharField(max_length=200)
    operation = models.CharField(max_length=200)
    value2 = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True,null=True)
    result = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def _str_(self):
        return self.result

