
from django.views.generic import ListView
from cover_page.models import Student


class StudentListView(ListView):
    
    # view to display list of the students
    
    model = Student
    template_name = 'studentCoverPage/home.html' # Specify template name
    context_object_name = 'students' # use this in the templates to access the list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Its a Class Function View'  # Additional context variable
        return context
    