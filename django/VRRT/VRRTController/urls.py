from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('SurveyInstance/', views.SurveyInstanceListView.as_view(), name='SurveyInstanceList')
]

urlpatterns += [
    path('SurveyInstance/create', views.SurveyCreate.as_view(), name='Survey_Instance_Create')
]

# urlpatterns += [
#     path('SurveyInstance/', views.SurveyInstanceListView.as_view(), name='SurveyInstanceList')
#     #path('SurveyInstance/<int:pk>', views.SurveyInstanceDetailView.as_view(), name='Survey-Instance-detail'),
# ]