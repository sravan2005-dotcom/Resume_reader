from django.db import models

# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=255)
    resume_file = models.FileField(upload_to='resumes/')
    eligibility_status = models.CharField(max_length=100, choices=[('Eligible', 'Eligible'), ('Not Eligible', 'Not Eligible')], default='Not Eligible')

    def __str__(self):
        return self.name