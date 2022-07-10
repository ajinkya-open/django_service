

from django.urls import path
from api.views import *
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

# register router 

urlpatterns=[

]


urlpatterns += router.urls
