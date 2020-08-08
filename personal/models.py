from django.db import models

# Create your models here.
# PRIORITY = [
#     ('L',"LOW"),
#     ('M',"MEDIUM"),
#     ('H',"HIGH"),
# ]

# class Question(models.Model):
#     title           = models.CharField(max_length=70)
#     question        = models.TextField()
#     priority        = models.CharField(max_length=1,choices=PRIORITY)

#     objects = models.Manager()

#     def __str__(self):
#         return self.title+"\n"+self.question

#     class Meta:
#         verbose_name = "The Question"
#         verbose_name_plural = "People's Questions"