from django.db import models

class ConferenceInfo(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField(1)

    def __str__(self):
        return '{}:{}'.format(self.name, self.year)

    class Meta:
        verbose_name = '会议信息'
        verbose_name_plural = verbose_name

class PaperInfo(models.Model):
    conference = models.ForeignKey(ConferenceInfo, on_delete=models.CASCADE, null=True, blank=True)
    paper_title = models.CharField(max_length=200)
    authors = models.CharField(max_length=300)
    abstract = models.CharField(max_length=5000)
    read_link = models.CharField(max_length=300, null=True, blank=True)
    pdf_link = models.CharField(max_length=300)
    affiliations = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        # return 'xxx'
        return '{},{}: {}'.format(self.conference.year, self.conference.name, self.paper_title)
    
    class Meta:
        verbose_name = '论文信息'
        verbose_name_plural = verbose_name
