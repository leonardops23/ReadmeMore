from blogs.models import Category, BlogPost
from django import forms

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    slug = forms.SlugField(max_length=100)
    available = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['slug'].widget.attrs.update({'class': 'form-control'})
        self.fields['available'].widget.attrs.update({'class': 'form-check-input'})

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        slug = cleaned_data.get('slug')
        if name and slug:
            if Category.objects.filter(name=name, slug=slug).exists():
                raise forms.ValidationError('Ya existe una categoría con el mismo nombre y slug.')

    class Meta:
        model = Category
        fields = ('name', 'slug', 'available',)


class PostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = '__all__'
    
