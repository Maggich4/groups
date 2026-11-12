from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
    def save(self, commit=True):
        user = super().save(commit=commit)
        
        if commit:
            group, created = Group.objects.get_or_create(
                name='Student'
            )
            
            user.groups.add(group)
        
        return user
    
    
class RegisterFormJKArman(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
    def save(self, commit=True):
        user = super().save(commit=commit)
        
        if commit:
            group, created = Group.objects.get_or_create(
                name='JSArman'
            )
            
            user.groups.add(group)
        
        return user
    
    
class RegisterFormChoice(UserCreationForm):
    
    role = forms.ChoiceField(
        choices=[
            ('Student', 'Student'),
            ('Teacher', 'Teacher')
        ]
    )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
    def save(self, commit=True):
            
            user = super().save(commit=commit)
            
            if commit:
                role = self.cleaned_data['role']
                group, created = Group.objects.get_or_create(
                    name=role
                )
                
                user.groups.add(group)
            
            return user