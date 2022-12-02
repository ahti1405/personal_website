from django.views.generic import TemplateView


class TodoView(TemplateView):
    template_name = 'todo/todo.html'
