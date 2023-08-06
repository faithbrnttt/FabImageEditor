from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from .models import Photo

class AccountLogin(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('photos')

class AccountRegister(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('photos')
    

    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(AccountRegister, self).form_valid(form)
    
class PhotoList(LoginRequiredMixin, ListView):
    model = Photo
    context_object_name = 'photos'

    def get_queryset(self):
       queryset = super().get_queryset().filter(user=self.request.user)
       query = self.request.GET.get("img")
       if query:
        queryset = queryset.filter(user__icontainer=self.request.user)
       return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = context['photos'].filter(user=self.request.user)
        return context
    

class PhotoDetail(LoginRequiredMixin, DetailView):
    model = Photo
    context_object_name = 'photo'
    template_name = 'base/photo.html'

class PhotoUpload(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['tag', 'img', 'description']
    success_url = reverse_lazy('photos')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PhotoUpload, self).form_valid(form)


class PhotoUpdate(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['tag', 'description']
    success_url = reverse_lazy('photos')
   
class PhotoDelete(LoginRequiredMixin, DeleteView):
    model = Photo
    context_object_name = 'photo'
    success_url = reverse_lazy('photos')
