from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class NewPassword(models.Model):
	app = models.CharField(max_length = 100)
	url = models.CharField(max_length = 100)
	app_username = models.CharField(max_length = 100)
	oldPassword = models.CharField(null= True, blank = True,max_length = 100)
	newPassword = models.CharField(max_length = 100)
	password_datetime = models.DateTimeField(default=timezone.now)
	vault_user_profile = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		if(self.app):
			return self.app + ", " + str(self.app_username)
		else:
			return str(self.app_username)

	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk': self.pk})

	def count_posts_of(user):
		return NewPassword.objects.filter(vault_user_profile=user).count()


class NewNote(models.Model):
	titulli = models.CharField(max_length=50, null= True, blank = True,verbose_name="Title")
	pershkrimi = RichTextUploadingField(max_length=1000, null= True, blank = True, verbose_name="Content", config_name='default')
	koha_posti = models.DateTimeField(default=timezone.now)
	files = models.FileField(upload_to = 'files', null= True, blank = True)
	vault_user_profile = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		if(self.titulli):
			return self.titulli + ", " + str(self.vault_user_profile)
		else:
			return str(self.vault_user_profile)

	def get_absolute_url(self):
		return reverse('note-detail', kwargs={'pk': self.pk})

	def count_posts_of(user):
		return NewNote.objects.filter(vault_user_profile=user).count()


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default = 'default.jpg', upload_to = 'profilePic')

	def __str__(self):
		return f'{self.user.username} Profile'

