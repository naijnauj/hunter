from django import forms
from .models import Article
#从form.py（对用户）提取校验规则
# class ArticleForm(forms.Form):
     # title = forms.CharField(label="标题",max_length=100)
     # content = forms.CharField(label="内容",max_length=100)
#从model.py（数据模型）提取校验规则
class ArticleForm(forms.ModelForm):
    class Meta:#固定为Meta
        model = Article #（从article数据模型中提取）
        fields = ['title','content'] 