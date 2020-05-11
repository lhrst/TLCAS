from django.db import models

class ConferenceInfo(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField(1)

class PaperInfo(models.Model):
    year = models.IntegerField()
    conference_name = models.CharField(max_length=50)
    paper_title = models.CharField(max_length=200)
    authors = models.CharField(max_length=300)
    abstract = models.CharField(max_length=5000)
    read_link = models.CharField(max_length=300)
    pdf_link = models.CharField(max_length=300)
    affiliations = models.CharField(max_length=300)
# Create your models here.
