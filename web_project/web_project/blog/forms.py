from django import forms

from web_project.blog.models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {
            'user_name': "Your Name",
            'user_email': 'Your Email',
            'text': 'Your Comment',
        }


class PostBaseForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ('title', 'excerpt', 'image', 'date', 'content', 'author')
        labels = {
            'title': 'Post Title',
            'excerpt': 'Excerpt',
            'image': 'Image',
            'date': 'Date',
            'content': 'Content',
            'author': 'Author',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Post title',
                }
            ),

            'excerpt': forms.TextInput(
                attrs={
                    'placeholder': 'Excerpt',
                }
            ),

            'image': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),

            'date': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            ),


            'content': forms.Textarea(
                attrs={
                    'placeholder': 'Add Content...',
                },
            ),

            # 'author': forms.TextInput(
            #     attrs={
            #         'placeholder': 'Author Name'
            #     }
            # )

        }


class PostCreateForm(PostBaseForm):
    pass
