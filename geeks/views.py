from django.shortcuts import render,HttpResponse
from django.views.generic  import TemplateView, FormView, ListView, UpdateView, DeleteView
from .forms import UserForm
from .models import User
# Create your views here.

class TemplateViews(TemplateView):
    template_name = 'index.html'

class form_view(FormView):
    template_name = 'form.html'
    form_class = UserForm
    success_url = "/"
    
    def get_context_data(self, **kwargs):
        context = super(form_view, self).form_valid(form)
        context = ['User']
        return context
    
    
    def form_valid(self,form):
        form.save()
        return super(form_view, self).form_valid(form)

class ListView(ListView):
    template_name = 'list.html'
    model = User
    context_object_name = 'persons'
    

    
class Updateview(UpdateView):
    template_name = 'update.html'
    fields = '__all__'
    model = User
    
class Deleteview(DeleteView):
    template_name = 'delete.html'
    model = User
    success_url = '/list_view'
    context_object_name = 'persons'
        
    
