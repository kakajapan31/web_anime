from django.shortcuts import render

# Create your views here.

from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib import  messages
from django.contrib.auth.models import User
from .models import Question, Choice
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import *
from .forms import CommentForm

def logout(request):
    auth_logout(request)
    messages.info(request, "See you later!")
    return redirect('index')

class Film_list_view(generic.ListView):
    template_name = 'web_film/index.html'
    context_object_name = 'list_film'
    model = Phim

    def get_queryset(self, *, objects_list=None, **kwargs):
        if 'search' in self.request.GET:
            query = self.request.GET['search']
            return Phim.objects.filter(ten_phim__icontains=query)
        return Phim.objects.all()[:8]

class Film_view(generic.DetailView):
    model = Phim
    template_name = "web_film/film_detail.html"
    context_object_name = 'film'
    form_class = CommentForm

    def post(self, request, pk):
        if request.POST.get('watch'):
            film_now = self.get_object()
            film_now.luot_xem += 1
            film_now.save()
            return redirect('film', pk)

        if request.POST.get('noi_dung'):
            self.object = self.get_object()
            form = CommentForm(request.POST, user=request.user, film=self.object,
                               noi_dung=request.POST['noi_dung'])
            if form.is_valid():
                form.save()
                messages.success(request, "just autofocus for comment!")
                return redirect('film', pk)
            else:
                messages.error(request, "You have not comment!")
                return redirect('film', pk)

class Author_view(generic.DetailView):
    model = Dao_dien
    template_name = 'web_film/author.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_film'] = Phim.objects.filter(dao_dien__in=[self.object])
        return context

class Actor_view(generic.DetailView):
    model = Dien_vien
    template_name = 'web_film/actor.html'
    context_object_name = 'actor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_film'] = Phim.objects.filter(dien_vien__in=[self.object])
        return context

class Genre_view(generic.DetailView):
     model = The_loai
     template_name = 'web_film/genre.html'
     context_object_name = 'genre'

     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['list_film'] = Phim.objects.filter(the_loai__in=[self.object])
         return context

@method_decorator(login_required, name='dispatch')
class Help(generic.TemplateView):
    template_name = 'web_film/help.html'

    def post(self, request):
        question = request.POST['question']
        if question != "":
            messages.success(request, "Thanks for your question, I will reply you soon!")
        else:
            messages.error(request, "You have not asked me :(")
        return redirect('help')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class About_me(generic.TemplateView):
    template_name = 'web_film/about_me.html'

class Login(generic.TemplateView):
    template_name = 'web_film/login.html'

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        next = request.GET.get('next', 'index')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.info(request, "Welcome " + user.first_name + " " + user.last_name + " to come back ")
            return redirect(next)
        else:
            messages.error(request, 'Username or password not correct, please try again.')
            return redirect(request.get_full_path())

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(*args, **kwargs)

class Register(generic.TemplateView):
    template_name = 'web_film/register.html'

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 != password2:
            messages.error(request, "Your passwords didn't match.")
            return redirect('register')
        elif len(password1) < 6:
            messages.error(request, "Your password must be more than or equal 6 characters")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Your email is used.")
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Your username is used.")
            return redirect('register')
        else:
            User.objects.create_user(username=username, email=email, password=password1, first_name=first_name,
                                     last_name=last_name)
        user = authenticate(request, username=username, password=password1)
        if user is not None:
            auth_login(request, user)
            messages.info(request, "Welcome new member " + user.first_name + " " + user.last_name)
            return redirect('index')

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(*args, **kwargs)

@method_decorator(login_required, name='dispatch')
class My_account(generic.TemplateView):
    template_name = 'web_film/my_account.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

@method_decorator(login_required, name='dispatch')
class Change_password(generic.TemplateView):
    template_name = 'web_film/change_password.html'

    def post(self, request):
        user = request.user
        current_password = request.POST['current_password']

        user_temp = authenticate(request=request, username=user.username, password=current_password)
        if user_temp is None:
            messages.error(request, "Current password is wrong!")
            return redirect('change_password')

        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            messages.error(request, "Password does not match!")
            return redirect('change_password')
        elif len(password1) < 6:
            messages.error(request, "The length of your password must be more than or equal 6 characters")
            return redirect('change_password')

        user.set_password(password1)
        user.save()
        messages.success(request, "You have changed your password successful!")
        user = authenticate(request=request, username=user.username, password=password1)
        auth_login(request, user)
        return redirect('change_password')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class Forgot_password(generic.TemplateView):
    template_name = 'web_film/forgot_password.html'

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        try:
            user = User.objects.get(username=username, email=email)
            if password1 != password2:
                messages.error(request, "Your password did not match")
                return redirect('forgot_password')
            else:
                messages.success(request, "You get new password successful")
                user.set_password(password1)
                user.save()
                user = authenticate(request=request, username=user.username, password=password1)
                auth_login(request=request, user=user)
                return redirect('forgot_password')
        except User.DoesNotExist:
            messages.error(request, "Your username or your email is wrong, try again!")
            return redirect('forgot_password')

class Question_view(generic.DetailView):
    template_name = 'web_film/question.html'
    model = Question
    context_object_name = 'question'

    def dispatch(self, request, pk):
        if pk > Question.objects.count():
            messages.error(request, "{}{}{}".format("I just have ", Question.objects.count(), " questions"))
            return  redirect('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = Question.objects.count()
        return context

    def post(self, request, pk):
        id_answer = request.POST.get('choice', None)
        if id_answer is None:
            messages.info(request, "You must to choose an answer")
            return redirect('question', pk)
        id_correct_answer = Question.objects.get(pk=pk).id_correct_answer
        if int(id_answer) == int(id_correct_answer):
            messages.success(request, "Correct!")
            return redirect('question', pk)
        else:
            messages.error(request, "Wrong answer :(")
            return redirect('question', pk)

