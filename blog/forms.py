from django import forms
from .models import Comment
from django.contrib.auth.models import User

class CommentForm(forms.Form):
	author = forms.CharField(max_length="250", required=False, widget=forms.TextInput(attrs={'placeholder':'Your name'}), error_messages={'required':'Leave your name'})
	text = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder':'Your comment', 'rows':5}), error_messages={'required':'Leave your comment'})

	def save(self, post_to, user):
		print (post_to)
		if (user.is_superuser):
			comm = Comment(author='Ludmila L', 
						   text=self.cleaned_data['text'],
						   post=post_to,
						   admin_added=True);
		else:
			comm = Comment(author=self.cleaned_data['author'], 
						   text=self.cleaned_data['text'],
						   post=post_to);
		comm.save()
		return True