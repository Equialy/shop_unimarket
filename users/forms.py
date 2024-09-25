from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class ProfileForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}), disabled=True)
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-input'}), disabled=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'image', 'date_birth', 'gender' ]
        labels = {
            'username': 'nickname',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'e-mail',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input',
                                                                            'placeholder': 'Введите имя пользователя'
                                                                            }))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'Введите пароль'}))
    gender = forms.ChoiceField(choices=User.GenderChoice.choices, widget=forms.RadioSelect,label='Пол', required=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'gender']
        labels = {
            'username': 'nickname',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'e-mail',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input',
                                                 'placeholder': 'Введите имя'
                                                 }),
            'last_name': forms.TextInput(attrs={'class': 'form-input',
                                                'placeholder': 'Введите фамилию'
                                                }),
            'email': forms.TextInput(attrs={'class': 'form-input',
                                            'placeholder': 'Введите email'
                                            })
        }

        def valid_email(self):
            valid = self.cleaned_data['email']
            if get_user_model().objects.filter(email=email).exists():
                raise forms.ValidationError('Такой email уже существует')
            return valid
