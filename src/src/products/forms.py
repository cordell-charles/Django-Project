from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	title		= forms.CharField(label= '', widget= forms.TextInput(attrs= {"placeholder": "your title"}))
	email 		= forms.EmailField()
	description = forms.CharField(
					required= False,
					widget= forms.Textarea(
						attrs={
							"placeholder": "your description",
							"class": "new-class-name two",
							"rows": 20,
							"cols": 120,
							"id": "my-id-for-text-area",
						}
					)
				)
	price		= forms.DecimalField(initial= 300000)
	class Meta:
		model = Product
		fields = {
			'title',
			'description',
			'price'
		}

	def clean_title(self, *args, **kwargs): # <my_field_name> 
		title = self.cleaned_data.get("title")
		if "CFE" not in title: # login written this way to input multiple errors if needed.
			raise forms.ValidationError("This is not a valid title")
		elif "news" not in title:
			raise forms.ValidationError("This is not a valid title")


	def clean_email(self, *args, **kwargs): # <my_field_name> 
		email = self.cleaned_data.get("email")
		if not email.endswith("com"):
			raise forms.ValidationError("This is not a valid email")
		return email
		
class RawProductForm(forms.Form):
	title		= forms.CharField(label= '', widget= forms.TextInput(attrs= {"placeholder": "your title"}))
	description = forms.CharField(
						required= False,
						widget= forms.Textarea(
							attrs={
								"placeholder": "your description",
								"class": "new-class-name two",
								"rows": 20,
								"cols": 120,
								"id": "my-id-for-text-area",
							}
						)
					)
	price		= forms.DecimalField()
