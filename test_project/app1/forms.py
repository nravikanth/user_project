# Import the forms library to create forms
from django import forms

# Import the TShirtRegistration model from the models.py
# in the current package
from .models import *

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = '__all__'


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'
"""
# Sample form with advance options
class studentRegistrationForm(forms.ModelForm):
	
	password1 = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = studentRegistration
		fields = '__all__'
 	
 	#overriding labels
	def __init__(self, *args, **kwargs):
	    super(studentRegistrationForm, self).__init__(*args, **kwargs)
	    self.fields['name'].label = "Your name:"
	    self.fields['email'].label = "Your email:"
	    self.fields['college_name'].label = "College Name:"
	    self.fields['address'].label = "Address"
	    self.fields['password1'].label = "Password:"
	    self.fields['password2'].label = "Confirm Password:"

	#overriding clean method
	def clean(self):
		cleaned_data = super(studentRegistrationForm, self).clean()
		password = cleaned_data.get("password1")
		confirm_password = cleaned_data.get("password2")
		if password != confirm_password:
			raise forms.ValidationError(
			"Oops!!! Password and confirm password are not matching... "
			)

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if not 'edu' in email:
			raise forms.ValidationError('Please use a valid .edu email address')
		return email

    
	def save(self,commit=False):
		instance = super(studentRegistrationForm,self).save(commit=commit)
		# you can do customization here
		instance.save()
		return instance
"""
