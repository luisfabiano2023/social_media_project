from django.urls import path
from . import views as vi


urlpatterns = [
    path('',vi.show,name='show')

]
