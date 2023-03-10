from django.db import models


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=200)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.TextField()


class Vacancy(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    salary = models.FloatField()


class Applicant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    condition = models.TextField()


class ListPost(models.Model):
    class Meta:
        unique_together = (('post_id', 'applicant_id'),)

    post_id = models.IntegerField(primary_key=True)
    applicant_id = models.IntegerField()
