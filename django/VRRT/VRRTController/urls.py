from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index')
]

urlpatterns += [
    path('SurveyInstance/', views.SurveyInstanceListView.as_view(), name='SurveyInstanceList'),
]

urlpatterns += [
    path('SurveyInstance/create', views.SurveyCreate.as_view(), name='Survey_Instance_Create'),
]

urlpatterns += [
    path('ExperinceSurvey/create', views.ExperinceSurveyCreate.as_view(), name='Experince_Survey_Instance_Create')
]

urlpatterns += [
    path('missionStatment', views.MissionStatmentView.as_view(), name="Mission_Statment"),
]

urlpatterns += [
    path('SiteIDList/', views.SiteListView.as_view(), name='Site_List_View')
]

urlpatterns += [
    path('logInRedirect', views.logInRedirect, name='logInRedirect'),
]

urlpatterns += [
    path('staffLandingPage', views.staffLandingPage.as_view(), name='staffLandingPage')
]

urlpatterns += [
    path('patientLandingPage', views.patientLandingPage.as_view(), name='patientLandingPage')
]



# urlpatterns += [
#     path('SurveyInstance/', views.SurveyInstanceListView.as_view(), name='SurveyInstanceList')
#     #path('SurveyInstance/<int:pk>', views.SurveyInstanceDetailView.as_view(), name='Survey-Instance-detail'),
# ]
