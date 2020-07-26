from django import forms

from blogs.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category',
                  'main_img', 'body', 'snippet')
