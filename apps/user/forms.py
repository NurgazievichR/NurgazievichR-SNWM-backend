from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = True
        user.is_staff = False  
        if commit:
            user.save()
        return user

