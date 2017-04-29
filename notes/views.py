from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Note
from django.shortcuts import redirect

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin



class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    redirect_field_name = 'notes:login_user'
    template_name = 'notes/home.html'
    context_object_name = 'all_notes'

    def get_queryset(self):
        return Note.objects.order_by('-date')[:40]

class DetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    redirect_field_name = 'notes:login_user'
    model = Note
    template_name = 'notes/detail.html'

class NoteCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'notes:login_user'
    model = Note
    fields = ['note_title', 'brief', 'body', 'note_logo']

class NoteUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'notes:login_user'
    model = Note
    fields = ['note_title', 'brief', 'body', 'note_logo']

class NoteDelete(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'notes:login_user'
    model = Note
    success_url = reverse_lazy('notes:home')

class UserFormView(View):
    form_class = UserForm
    template_name = 'notes/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned/ normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User Objects if credentioals are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('notes:home')
        return render(request, self.template_name, {'form': form})

def logout_user(request):
    logout(request)
    return redirect('notes:home')


    # process form data
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('notes:home')
        else:
            return render(request, 'notes/login_form.html', {'error_message': 'Invalid Login Credentials'})
    return render(request, 'notes/login_form.html')














