from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, FormView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.
from django.contrib import messages


class HomePageView(TemplateView):

    template_name = 'SocialApp/Issue_list.html'
    b_form = BusinessModelForm
    s_form = SocialIssueForm
    model = SocialIssue
    login_form = AuthenticationForm
    sign_form = SignUpForm

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['SocialIssue_list'] = SocialIssue.objects.all()
        context['business_list'] = BusinessPost.objects.all()
        # if self.request.user.username:
        context['b_form'] = self.b_form
        context['s_form'] = self.s_form
        context['login_form'] = self.login_form
        context['sign_form'] = self.sign_form
        return context

    # def post(self, request, *args, **kwargs):
    #     if request.method == 'POST':
    #         b_form = BusinessModelForm(request.POST, request.FILES)
    #         s_form = SocialIssueForm(request.POST, request.FILES)
    #
    #         if not self.request.user.username:
    #             messages.error(request, "kindly Login to proceed!")
    #             return HttpResponseRedirect(reverse('SocialApp:homepage'))
            # if s_form.is_valid():
    #             s_form.save()
    #             return HttpResponseRedirect(reverse('SocialApp:homepage'))
    #         elif b_form.is_valid():
    #             b_form.save()
    #             return HttpResponseRedirect(reverse('SocialApp:homepage'))

# def dashboard(request):
#
#     return render(request,'SocialApp/Issue_list.html' , {'login_form': AuthenticationForm,
#         'sign_form': SignUpForm,
#         'user': request.user})

def signup(request):

        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                messages.success(request, 'successfully sign up!!!')

                return HttpResponseRedirect(reverse('SocialApp:homepage'))
        else:
            form = SignUpForm()

        messages.error(request, 'Something Went wrong Try again!!!')
        return HttpResponseRedirect(reverse('SocialApp:homepage'))

def login_user(request):

        username = password = ''
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user )
                messages.success(request, 'You are successfully login')
                return HttpResponseRedirect(reverse('SocialApp:homepage'))

        messages.error(request, 'Something Went wrong Try again')
        return HttpResponseRedirect(reverse('SocialApp:homepage'))

def logout_view(request):
        logout(request)
        return HttpResponseRedirect(reverse('SocialApp:homepage'))


def sformview(request):
    if request.method == 'POST':
        s_form = SocialIssueForm(request.POST, request.FILES)
        if not request.user.username:
            messages.error(request, "kindly Login to proceed!")
            return HttpResponseRedirect(reverse('SocialApp:homepage'))

        if s_form.is_valid():
            s_form.save()
        return HttpResponseRedirect(reverse('SocialApp:homepage'))


def bformview(request):
    if request.method == 'POST':
        b_form = BusinessModelForm(request.POST, request.FILES)
        if not request.user.username:
            messages.error(request, "kindly Login to proceed!")
            return HttpResponseRedirect(reverse('SocialApp:homepage'))

        # s_form = SocialIssueForm(request.POST, request.FILES)

        if b_form.is_valid():
            b_form.save()
        return HttpResponseRedirect(reverse('SocialApp:homepage'))
