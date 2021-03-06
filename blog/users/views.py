from tkinter.tix import Form
from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm
# Create your views here.


def index(request):
    return render(request, 'blogs/blog.html')


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = '/'


class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.user_id
        return super().form_valid(form)


def logout(request):
    if 'user' in request.session:
        del (request.session['user'])

    return redirect('/')
