from django.urls import path

#FBVs
from .views.funcBased import coverPage

#CBVs
from .views.classBased import StudentListView



urlpatterns = [
    #FBVs
    path('func/', coverPage, name='students'),
    
    
    #CBVs
    path('class/', StudentListView.as_view(), name='Student_class'),
]