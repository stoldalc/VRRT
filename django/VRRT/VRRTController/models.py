from django.db import models

# Create your models here.


from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Survey(models.Model):
    """Survey model"""

    #Name of survey based on location
    SurveyName = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.SurveyName
    
    # def get_absolute_url(self):
    #     """Returns the url to access a detail record for this book."""
    #     return reverse('book-detail', args=[str(self.id)])


import uuid #Required for unique survey instances

class SurveyInstance(models.Model):
    """Model reprsenting a specic instance of a survey"""

    #Survey object
    survey = models.ForeignKey('Survey',on_delete=models.SET_NULL, null=True)

    #ID for the specfic survey instance
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular survey')

    #Pain score at start of session
    PainScoreStart = models.IntegerField()

    #Pain score at end of session
    PainScoreEnd = models.IntegerField()

class SiteID(models.Model):
    """A model that describes the VA location"""

    SiteName = models.CharField(max_length=200, help_text='Enter the site location or name')

    def __str__(self):
        """String that reprsents the model object."""

        return self.SiteName


