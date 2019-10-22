from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):


	title		= forms.CharField(
					required= True,
					label= '', 
					widget= forms.TextInput(
						attrs= {
							"placeholder": "Your Main title"
						}
					)
				)
	subtitle 	= forms.CharField(
					required= True, 
					widget= forms.TextInput(
						attrs= {
							"placeholder": "Brief description of article"
						}
					)
				)
	article 	= forms.CharField(
					required= True,
					widget= forms.Textarea(
						attrs= {
							"placeholder": "Your story",
							"rows": 40,
							"cols": 120,
						}
					)
				)
	name 		= forms.CharField(required= True)

	class Meta:
	    model = Article
	    fields = {
	        'title',
	        'subtitle',
	    	'article',
	    	'name'}