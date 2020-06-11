from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

from .views import (
	PasswordCreateView, 
	PasswordDetailView, 
	PasswordListView, 
	UpdatePasswordView, 
	DeletePasswordView,
	NoteListView,
	NoteDetailView,
	UpdateNoteView,
	DeleteNoteView,
	NoteCreateView
	)

urlpatterns = [
	path('', views.home, name='app-home'),
	path('passwords/<str:username>/', PasswordListView.as_view(), name='passwords-page'),
	path('notes/<str:username>/', NoteListView.as_view(), name='notes-page'),
	path('pass-detail/<int:pk>/', PasswordDetailView.as_view(), name='detail'),
	path('note-detail/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
	path('pass/create/', views.generate_password, name='generate'),
	path('pass/view/', views.view_password, name='view'),
	path('pass/save/', PasswordCreateView.as_view(template_name='theVault/newpassword_form.html'), name='save'),
	path('update/<int:pk>/', UpdatePasswordView.as_view(template_name='theVault/newpassword_form.html'), name='update-password'),
	path('note-update/<int:pk>/', UpdateNoteView.as_view(template_name='theVault/newNote_form.html'), name='update-note'),
	path('delete/<int:pk>/', DeletePasswordView.as_view(template_name='theVault/confirm_delete.html'), name='delete-password'),
	path('note-delete/<int:pk>/', DeleteNoteView.as_view(template_name='theVault/note_confirm_delete.html'), name='delete-note'),
	path('about/', views.about, name='app-about'),
	path('about-2/', views.about_2, name='app-about-2'),
	path('signup/', views.UserRegister, name='sign-up'),
	path('profile/', views.user_profile, name='profile'),
	path('newNote/', NoteCreateView.as_view(template_name='theVault/newNote_form.html'), name='create-note'),
	# path('new-password/', views.generate_password, name='newPassword'),
]

if(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)