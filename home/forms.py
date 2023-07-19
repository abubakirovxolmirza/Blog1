from django import forms
from .models import Profile, BlogPost


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)


class BlogPostForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of the Blog'})
    )
    slug = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Do not write a number here'})
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content of the Blog'})
    )

    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'content', 'image')

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if BlogPost.objects.filter(slug=slug).exists():
            raise forms.ValidationError("A blog post with this slug already exists.")
        return slug
