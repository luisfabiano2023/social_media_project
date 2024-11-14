from django.urls import path
from . import views as vi


urlpatterns = [
    path('',vi.show,name='show'),
    path('lst',vi.ls_u,name='nme'),
    path('ct',vi.ct_u,name='ct'),

]
