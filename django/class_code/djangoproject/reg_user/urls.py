from django.conf.urls import url
from reg_user import views

app_name = 'reg_user'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]