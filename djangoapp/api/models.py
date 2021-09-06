from django.db import models

# Create your models here.
# POST = create/insert/add
# GET = retrieve/fetch
# PUT = update/edit
# DELETE = remove/delete

class Employee(models.Model):
    fullName = models.CharField(max_length=100)
    empCode = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)


