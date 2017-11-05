#coding=utf-8  
from django.shortcuts import render
from django.shortcuts import redirect
from block.models import Block
from .models import Article
from .forms import ArticleForm

def article_list(request,block_id):
   block_id = int(block_id)
   block = Block.objects.get(id=block_id)
   articles_objs = Article.objects.filter(block=block,status=0).order_by("-id")
   return render(request,"article_list.html",{"articles":articles_objs,"b":block})

   
def article_create(request,block_id):
   block_id = int(block_id)
   block = Block.objects.get(id=block_id)
   if request.method == "GET":
      return render(request,"article_create.html",{"b":block})
   else:
       #加入校验器之前
       # title = request.POST["title"]
       # content = request.POST["content"]
       # if not (title and content):
           # return render(request,"article_create.html",
                   # {"b":block,"error":"标题和内容都不能为空",
                    # "title":title,"content":content})
       # if len(title)>100 or len(content)>10000:
           # return render(request,"article_create.html",
                   # {"b":block,"error":"标题或内容太长了",
                    # "title":title,"content":content})
       # article = Article(block=block,title=title,content=content,status=0)
       # article.save()
       # return redirect("/article/list/%s" %block_id)#重定向（302)到参数
       
       #加入校验器之后
       # form = ArticleForm(request.POST)
       # if form.is_valid():#判定参数合法性
           # article = Article(block=block,title=form.cleaned_data["title"],
                             # content=form.cleaned_data["content"],status=0)
           # article.save()
           # return redirect("/article/list/%s" %block_id)#重定向（302)到参数
       # else:
           # return render(request,"article_create.html",{"b":block,"form":form})#传回页面
       #进一步进化，因为数据来源于model数据模型，而我们恰好创建model（归属article）的一个实例
       form = ArticleForm(request.POST)
       if form.is_valid():#判定参数合法性
           article = form.save(commit=False)#commit决定是否存入数据库，由于缺失block，暂不存入
           article.block = block
           article.status = 0
           article.save()
           return redirect("/article/list/%s" %block_id)#重定向（302)到参数
       else:
           return render(request,"article_create.html",{"b":block,"form":form})#传回页面
   
   
   
