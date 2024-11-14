from django.urls import path
from . import views as vi


urlpatterns = [
    path('show',vi.show,name='show')


]
