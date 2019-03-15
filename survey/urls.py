from . import views
from django.conf.urls import url


# SET THE NAMESPACE!
app_name = 'survey'
# Be careful setting the name to just /login use userlogin instead!

urlpatterns = [

    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^survey_detail/$', views.EmployeeSurveys.as_view(), name='survey_detail'),

]
