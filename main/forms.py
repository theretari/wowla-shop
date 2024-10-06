from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
    
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)
    
    def clean_desc(self):
        desc = self.cleaned_data["vdescription"]
        return strip_tags(desc)