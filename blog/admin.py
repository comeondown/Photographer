from django.contrib import admin
from .models import Post, Comment
from django import forms
from redactor.widgets import RedactorEditor

class PostAdminForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = '__all__'
		widgets = {
			'text': RedactorEditor(),
		}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	form = PostAdminForm

	def comments(self, obj):
		html = ''
		comms = obj.comment_set.all()
		for c in comms:
			html = html + "<a href=" + "'/admin/blog/comment/" + str(c.id) + "'" +  ">" + c.author + "\n" + c.text + "</a>" + "<br/>"
		return html

	comments.allow_tags = True

	list_display = ['id','date_created', 'title', 'text', 'description', 'hide']
	readonly_fields = ('date_created', 'comments')
	fieldsets = (
		(None, { 'fields' : ('date_created', 'title', 'text', 'description', 'hide')}),
		('Comment', {'classes':('collapse',),
					'fields': ('comments',)})
		)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	fields = ['text', 'post', 'date_created', 'hide']
	readonly_fields = ('post', 'date_created',)
	list_display = ['date_created', 'text', 'post']
