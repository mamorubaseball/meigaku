from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.password_validation import validate_password
from .models import Circles,CircleContents,ParentCategory,Category
from django.contrib.auth import authenticate
from django.contrib import messages


class CircleRegistForm(forms.ModelForm):
    username = forms.CharField(label='サークル名',widget=forms.TextInput(
            attrs={'placeholder':'ユーザ名'}))
    password = forms.CharField(label='パスワード')
    repassword = forms.CharField(label='パスワード再入力')
    email = forms.EmailField(label='メールアドレス',widget=forms.TextInput(
            attrs={'placeholder':'大学のアドレスを入力'}))

    class Meta:
        model=Circles
        fields=['username','password','repassword','email']

    def clean_password(self):
        password = self.cleaned_data['password']
        password2 = self.data.get('repassword')
        if password != password2:
            raise forms.ValidationError('パスワードが一致しません。')
        return password

    def save(self, commit=False):
        circle=super().save(commit=False)
        validate_password(self.cleaned_data['password'],circle)
        circle.set_password(self.cleaned_data['password'])
        circle.save()
        return circle

class CircleLoginForm(forms.Form):
    username = forms.CharField(label='サークル名')
    password = forms.CharField(label='パスワード',widget=forms.PasswordInput())
    # password = forms.CharField(label='パスワード')

class CircleContentUpdateForm(forms.ModelForm):
    # 親カテゴリの選択欄がないと絞り込めないので、定義する。モデルフォームに通常のフィールドを新しく追加。
    category_data=Category.objects.all()
    category_choice={}
    for category in category_data:
        category_choice[category]=category

    category=forms.ChoiceField(label='カテゴリ',widget=forms.Select,choices=list(category_choice.items()))
    class Meta:
        model=CircleContents
        # fields='__all__'
        fields=['category','contents','how_often','event','place','money','member','how_often_drink','twitter_url','instagram_url','picture']












