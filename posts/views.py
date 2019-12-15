from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
from .models import Comments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm

# Create your views here.
def index(request):
    #return HttpResponse('Samuel Congrats on your first post')
    num = 0
    comments = Comments.objects.all()
    for comment in comments:
        if comment.post_comment_id == 8:
            num += 1

    posts = Posts.objects.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]
    #posts = paginator.get_page(page)
    contex = {
        'page_range': page_range,
        'posts': posts,
        'items': items,
        'comments':comments,
        'num': num
    }
    return render(request, 'posts/index.html', contex)

def details(request, id):

    posts = Posts.objects.get(id=id)
    comments = Comments.objects.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid:
            comment_form.save()
            comment_form = CommentForm(request.POST)
    else:
        comment_form = CommentForm()
    
    contex = {
        'title': 'news',
        'posts': posts,
        'comments': comments,
        'comment_form': comment_form
    }

    return render(request, 'posts/details.html', contex)