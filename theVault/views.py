from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import NewPassword, NewNote
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import vault_users, UserUpdate, ProfileUpdate, newNoteForm
from django.contrib import messages
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.
import string
import random

@login_required(redirect_field_name='theVault/signup.html')
def home(request):
	return render(request, 'theVault/home.html')


class PasswordListView(LoginRequiredMixin, ListView):
	model = NewPassword
	template_name = "theVault/password-list.html"
	context_object_name = 'vault_NewPasswordData'
	ordering = ['-password_datetime']

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return NewPassword.objects.filter(vault_user_profile=user).order_by('-password_datetime')


class NoteListView(LoginRequiredMixin, ListView):
	model = NewNote
	template_name = "theVault/viewNotes.html"
	context_object_name = 'vault_NewNotes'
	ordering = ['-koha_posti']

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return NewNote.objects.filter(vault_user_profile=user).order_by('-koha_posti')

class NoteDetailView(LoginRequiredMixin, DetailView):
	model = NewNote
	template_name = "theVault/note-detail.html"


@login_required(redirect_field_name='theVault/signup.html')
def about(request):
	return render(request, 'theVault/about.html')


def about_2(request):
	return render(request, 'theVault/about-2.html')


def UserRegister(request):
	if(request.method == 'POST'):
		form = vault_users(request.POST)
		if(form.is_valid()):
			form.save()
			username = form.cleaned_data.get('username')
			return redirect('login')
	else: 
		form = vault_users()
	return render(request, 'theVault/signup.html', {'form':form})

@login_required(redirect_field_name='theVault/home.html')
def user_profile(request):
	num_notes = NewNote.objects.filter(vault_user_profile=request.user).count()
	num_passwords = NewPassword.objects.filter(vault_user_profile=request.user).count()
	if(request.method == 'POST'):
		user_form = UserUpdate(request.POST, instance=request.user)
		profile_form = ProfileUpdate(request.POST, request.FILES, instance=request.user.profile)
		if(user_form.is_valid() and profile_form.is_valid()):
			user_form.save()
			profile_form.save()
			messages.success(request, f'Your information has been updated!')
			return redirect('profile')
	else: 
		user_form = UserUpdate(instance=request.user)
		profile_form = ProfileUpdate(instance=request.user.profile)

	te_dhenat_profili = {
		'user_form':user_form,
		'profile_form': profile_form,
		'num_passwords': num_passwords,
		'num_notes': num_notes,
	}
	return render(request, 'theVault/profile.html', te_dhenat_profili)


@login_required(redirect_field_name='theVault/signup.html')
def generate_password(request):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	characters = list(alphabet)
	length = int(request.GET.get('length', 12))

	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

	if request.GET.get('numbers'):
		characters.extend(list('0123456789'))

	if request.GET.get('special'):
		characters.extend(list('!@#$%^&*?'))

	thepassword = ''
	for x in range(length):
		thepassword += random.choice(characters)

	return render(request, 'theVault/newpassword_generated.html', {'password': thepassword})


@login_required(redirect_field_name='theVault/signup.html')
def view_password(request):
	context = {
		'options': range(12, 65),
	}

	print(context['options'])
	return render(request, 'theVault/generate_password.html', context)

class PasswordCreateView(LoginRequiredMixin, CreateView):
	model = NewPassword
	fields = ['app','url','app_username','oldPassword', 'newPassword']

	def form_valid(self, form):
		form.instance.vault_user_profile = self.request.user
		return super().form_valid(form)



class PasswordDetailView(LoginRequiredMixin, DetailView):
	model = NewPassword
	template_name = "theVault/password-detail.html"



class UpdatePasswordView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = NewPassword
    fields = ['app','url','app_username','oldPassword', 'newPassword']

    def post_form_valid(self, form):
        form.instance.vault_user_profile = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if(self.request.user == post.vault_user_profile):
            return True
        return False


class DeletePasswordView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = NewPassword
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if(self.request.user == post.vault_user_profile):
            return True
        return False

class NoteCreateView(LoginRequiredMixin, CreateView):
	model = NewNote
	fields = ["titulli","pershkrimi","files"]

	def form_valid(self, form):
		form.instance.vault_user_profile = self.request.user
		return super().form_valid(form)



class UpdateNoteView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = NewNote
    fields = ["titulli","pershkrimi","files"]

    def post_form_valid(self, form):
        form.instance.vault_user_profile = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if(self.request.user == post.vault_user_profile):
            return True
        return False


class DeleteNoteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = NewNote
    success_url = '/'
	
    def test_func(self):
        post = self.get_object()
        if(self.request.user == post.vault_user_profile):
            return True
        return False