from blogs.models import Category, BlogPost
from django import forms
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    slug = forms.SlugField(max_length=100)
    available = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['slug'].widget.attrs.update({'class': 'form-control'})
        self.fields['available'].widget.attrs.update({'class': 'form-check-input'})

    class Meta:
        model = Category
        fields = ('name', 'slug', 'available',)


class PostForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['author'].widget.attrs.update({'class': 'form-control'})
        self.fields['short_content'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control'})
        self.fields['featured_image'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_featured'].widget.attrs.update({'class': 'form-check-input'})

    class Meta:
        model = BlogPost
        fields = ('title', 'category', 'author', 'short_content', 'content', 'featured_image', 'status', 'is_featured',)
    
