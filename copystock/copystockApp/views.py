from django.shortcuts import render, redirect
from django.http import Http404

from . import models


# トップページ（部屋の一覧）
def index(request):
    template_name = "copystockApp/index.html"
    context = {"articles": models.Article.objects.all()}
    return render(request, template_name, context)


# 部屋の作成
def new(request):
    template_name = "copystockApp/new.html"
    if request.method == "POST":
        article = models.Article.objects.create(title=request.POST["title"])
        return redirect(view_article, article.pk)
    
    return render(request, template_name)


# 部屋の詳細ページ
def view_article(request, pk):
    template_name = "copystockApp/view_article.html"
    try:
        article = models.Article.objects.get(pk=pk)
    except models.Article.DoesNotExist:
        raise Http404
    
    if request.method == "POST":
        # データベースに投稿されたキャッチコピーを保存
        models.Copy.objects.create(text=request.POST["text"], article=article)
    
    context = {"article": article}
    return render(request, template_name, context)

# 部屋の編集ページ
def edit(request, pk):
    template_name = "copystockApp/edit.html"
    try:
        article = models.Article.objects.get(pk=pk)
    except models.Article.DoesNotExist:
        raise Http404

    if request.method == "POST":
        article.title = request.POST["title"]
        article.save()
        return redirect(view_article, pk)
    
    context = {"article": article}
    return render(request, template_name, context)

# 部屋の削除
def delete(request, pk):
    try:
        article = models.Article.objects.get(pk=pk)
    except models.Article.DoesNotExist:
        raise Http404

    article.delete()
    return redirect(index)