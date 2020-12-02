from django.shortcuts import render
from VRRTController.models import Survey, SurveyInstance, SiteID

# Create your views here.

def index(request):
    """View function for home page of site"""

    #Generate count fo rthe number of active sites
    num_Sites = SiteID.objects.all().count()

    #Generate counts for number of survey types
    num_Surveys = Survey.objects.all().count()

    #Generate counts of number of surveys taken
    num_Surveys_Submitted = SurveyInstance.objects.all().count()

    context = {
        'num_Sites': num_Sites,
        'num_Surveys': num_Surveys,
        'num_Surveys_Submitted':num_Surveys_Submitted,
    }

    return render(request,'index.html',context=context)


from django.views import generic

class SurveyInstanceListView(generic.ListView):
    model = SurveyInstance 
    

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class SurveyCreate(CreateView):
    model = SurveyInstance
    fields = ['PainScoreStart','PainScoreEnd', 'HeartRateStart', 
        'HeartRateEnd', 'BPStartValue1', 'BPStartValue2', 
        'BPEndValue1', 'BPEndValue2', 'O2SaturationStart',
        'O2SaturationEnd']
    success_url = reverse_lazy('index')