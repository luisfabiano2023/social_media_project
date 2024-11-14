from django.urls import path
from . import views as vi


urlpatterns = [
    path('',vi.show,name='show'),
    path('lst',vi.lsu,name='nme'),
    path('ct',vi.ctu,name='ct'),

]
