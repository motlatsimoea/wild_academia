from feed.views import post
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Tag
from feed.models import Feed
from accounts.models import MyUser
from .forms import PostCreateForm, CommentForm
from django.views.generic import ListView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.contrib import messages





def base(request):
   return {'tags': Tag.objects.all(),
            
   }

def about(request):

    return render(request, 'blog/about.html')



def home(request):
    questions   = Post.objects.all().order_by('-date_posted')

    return render(request, 'blog/home.html', {'questions': questions})


@login_required
def create_post(request):
    tag_objs = []

    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            title   = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            tags    = form.cleaned_data.get('tags')

           
            tag_list = list(tags.split(','))
            for tag in tag_list:
                t, created  = Tag.objects.get_or_create(title=tag)
                tag_objs.append(t)

            p, created = Post.objects.get_or_create(title=title, content=content, document=request.FILES.get('document'), author=request.user)
            p.tags.set(tag_objs)
            p.save()
            messages.success(request, 'question created!')
            return redirect('questions')
        
    else:
        form = PostCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'blog/post_create.html', context)



#@login_required
def post_detail(request, pk=None):
    post        = get_object_or_404(Post, pk=pk)
    comments     = Comment.objects.filter(post=post).order_by('-id')

    if request.method == 'POST':
        comment_form    = CommentForm(request.POST or None)
        
        if comment_form.is_valid():
            content     = request.POST.get('content')
            comment = Comment.objects.create(post=post, user=request.user, content=content)
            comment.save()

    else:
        comment_form = CommentForm()
        
        

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,    
    }

    if request.is_ajax():
        html    = render_to_string('blog/comments.html', context, request=request)
        return JsonResponse({'form': html})
    return render(request,'blog/post_detail.html', context)




def tags(request, tag_slug):
    tag         = get_object_or_404(Tag, slug=tag_slug)
    posts       = Post.objects.filter(tags=tag).order_by('-date_posted')
    feeds       = Feed.objects.filter(tags=tag).order_by('-date_posted')


    context     = {
        'tag': tag,
        'posts': posts,
        'feeds': feeds,
    }

    return render(request, 'blog/tags.html', context)





class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Post
    fields = ['title', 'content', 'tags']
    template_name = 'blog/post_create.html'
    context_object_name = 'post'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model   = Comment

    def get_success_url(self):
        post = self.object.post
        return reverse_lazy('post-detail', kwargs={'pk': post.id})
    
    
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.user:
            return True
        return False
