from django.urls import include , path
from random_tokens import views 
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register(r'generate-tokens', views.GenerateTokenViewSet , basename='Tokens')
#router.register(r'assign-token', views.StatesViewSet , basename='StateMaster')
#router.register(r'unblock-token', views.StatesViewSet , basename='StateMaster')
#router.register(r'delete-token', views.StatesViewSet , basename='StateMaster')
#router.register(r'assign-token', views.StatesViewSet , basename='StateMaster')



from django.conf.urls import url 
 
urlpatterns = [ 
    url(r'^generate-tokens/$', views.generate_token),
    url(r'^delete-token/(?P<token>.*)$', views.delete_token),
    url(r'^assign-token/', views.assign_token),
    url(r'^unblock-token/(?P<token>.*)$', views.unblock_token),
    url(r'^keep-alive-token/(?P<token>.*)$', views.keep_alive_token)
]

