from django.db import models
from redactor.fields import RedactorField
from django.utils.html import strip_tags

class Post(models.Model):
	date_created = models.DateTimeField(auto_now_add=True, blank=False, null=False)
	title = models.CharField(max_length=1000, blank=False, null=False)
	description = models.CharField(max_length=1000, blank=True, null=True)
	text = RedactorField(verbose_name='Text')
	hide = models.BooleanField(default = False)

	def __str__(self):
		return "{}".format(strip_tags(self.text[0:150]))

class Comment(models.Model):
	author = models.CharField(max_length=300, blank=False, null=False)
	date_created = models.DateTimeField(auto_now_add=True, blank=False, null=False)
	post = models.ForeignKey('Post', default=None)
	text = models.TextField()
	hide = models.BooleanField(default = False)
	admin_added = models.BooleanField(default = False)

	def __str__(self):
		return "{}".format(self.text[0:150])
