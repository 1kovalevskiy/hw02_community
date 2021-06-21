from django.shortcuts import render, get_object_or_404

from .models import Group, Post


def index(request):
    latest = Post.objects.all()[:11]
    return render(request, "index.html", {"posts": latest})


# view-функция для страницы сообщества
def group_posts(request, slug):
    """
    функция get_object_or_404 получает по заданным критериям объект из базы
    данных или возвращает сообщение об ошибке, если объект не найден
    """
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления условия WHERE group_id = {group_id}
    # posts = Post.objects.filter(group=group).order_by("-pub_date")[:12]
    return render(request, "group.html", {"group": group, "posts": posts})


# view-функция со списком сообществ
def group_list(request):
    groups = Group.objects.all()
    return render(request, "group_list.html", {"groups": groups})
