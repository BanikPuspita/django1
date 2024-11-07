from cover_page.models import Student
from django.shortcuts import render

def coverPage(request):
    students = Student.objects.all()
    
    context = {
        'students': students,
        'message': 'Its a Function Based View'
    }
    
    return render(request, 'studentCoverPage/home.html', context)
