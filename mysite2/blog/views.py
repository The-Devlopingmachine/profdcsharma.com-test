from django.core import paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View, ListView, DeleteView, DetailView
from django.template.defaultfilters import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Post
from .forms import Postform 

from taggit.models import Tag

# Create your views here.


class new_post(LoginRequiredMixin, View):
    # Defining the templates and the initial fiels values
    template_name = "blog/new_post.html"
    raise_exception=True
    permission_denied_message = "You are not allowed here"
    form_class = Postform
    initial = {
        'title': 'Enter your title here',
        'discreption': 'The post Discreption'
    }

    def get(self, request):
        form = self.form_class(initial = self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.slug = slugify(newpost.title)
            newpost.save()
            form.save_m2m()
            return redirect('blog:home')
        return render(request, self.template_name, {'form': form})

class Home_view(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 18
    queryset = Post.objects.all()

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Post.tags.most_common()[:4]
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'common_tags': common_tags,
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post_related = post.tags.similar_objects()
    context = {
        'post': post,
        'post_related': post_related,
    }
    return render(request, 'blog/post_detail.html', context)
