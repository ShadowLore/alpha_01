from django.shortcuts import render
from django.db.models import Q
from .models import Post, Comment
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import NewCommentForm


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home_page.html', context)


def about(request):
    return render(request, 'blog/about_page.html')


class PostListView(ListView):
    model = Post
    template_name = 'blog/home_page.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 7


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = Comment.objects.filter(
            post_connected=self.get_object()).order_by('-date_posted')
        data['comments'] = comments_connected
        if self.request.user.is_authenticated:
            data['comment_form'] = NewCommentForm(instance=self.request.user)

        return data

    def post(self, request, *args, **kwargs):
        new_comment = Comment(content=request.POST.get('content',),
        author=self.request.user, post_connected=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'blog/post_delete.html'
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class SearchView(View):
    def get(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        query = request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
            ).distinct()
        context = {
            'queryset': queryset
        }
        return render(request, 'blog/search_bar.html', context)


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'blog/search_bar.html', context)


def soobin(request):
    return render(request, 'artists/soobin.html')


def yeongjun(request):
    return render(request, 'artists/yeongjun.html')


def taehyun(request):
    return render(request, 'artists/taehyun.html')


def beomgyu(request):
    return render(request, 'artists/beomgyu.html')


def huening_kai(request):
    return render(request, 'artists/huening_kai.html')

