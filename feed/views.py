from django.shortcuts import render, get_object_or_404
from .models import Feed, FeedImage, Opinion, Stream, Like
from blog.models import Tag
from .forms import OpinionForm
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.template import loader
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.contrib import messages


def post(request):
    feeds    = Feed.objects.all().order_by('-date_posted')

    context = {
        'posts': feeds,
    }

    return render(request, 'feed/posts.html', context)




@login_required
def create_feed(request):
    tag_objs = []
    if request.method == 'POST':
        length      = request.POST.get('length')
        title       = request.POST.get('title')
        content     = request.POST.get('content')
        tags        = request.POST.get('tags')

        if tags:
            tag_list = list(tags.split(','))
            for tag in tag_list:
                t, created  = Tag.objects.get_or_create(title=tag)
                tag_objs.append(t)

            feed, created = Feed.objects.get_or_create(title=title, content=content, author=request.user)
            feed.tags.set(tag_objs)
            feed.save()
        else:
            feed, created = Feed.objects.get_or_create(title=title, content=content, author=request.user)
            feed.save()
            
        for file_num in range(0, int(length)):
            FeedImage.objects.create(
                feed=feed,
                media = request.FILES.get(f'media{file_num}')
            ) 
            
    return render(request, 'feed/feed_create.html')




@login_required
def stream(request):
    user        = request.user
    feeds       = Stream.objects.filter(user=user)

    group_ids   = []
    for feed in feeds:
        group_ids.append(feed.feed_id) 

    feed_items  = Feed.objects.filter(id__in=group_ids).all().order_by('-date_posted')

    template    = loader.get_template('feed/stream.html')

    context = {
        'feed_items': feed_items,
    }

    return HttpResponse(template.render(context, request))





#@login_required
def feed_details(request, pk=None):
    feed        = get_object_or_404(Feed, pk=pk)
    opinions    = Opinion.objects.filter(feed=feed, reply=None).order_by('-id')

    if request.method == 'POST':
        opinion_form    = OpinionForm(request.POST or None)
        if opinion_form.is_valid():
            content     = request.POST.get('content')
            reply_id    = request.POST.get('opinion_id')
            opinion_qs  = None
            if reply_id:
                opinion_qs = Opinion.objects.get(id=reply_id)
            opinion = Opinion.objects.create(feed=feed, user=request.user, content=content, reply=opinion_qs)
            opinion.save()

    else:
        opinion_form = OpinionForm()

    context = {
        'feed': feed,
        'opinions': opinions,
        'opinion_form': opinion_form,
    }

    if request.is_ajax():
        html    = render_to_string('feed/opinions.html', context, request=request)
        return JsonResponse({'form': html})
    return render(request,'feed/feed_detail.html', context)



@login_required
def like_feed(request):
    user = request.user
    if request.method == 'POST':
        feed_id = request.POST.get('id')
        feed    = Feed.objects.get(id=feed_id)

        liked = False
        if user in feed.likes.all():
            feed.likes.remove(user)
            liked = False
        else:
            feed.likes.add(user)
            liked = True

        like, created = Like.objects.get_or_create(user=user, feed_id=feed_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        else:
            like.value = 'Like'

        feed.save()	
        like.save()


    context = {
        'value': like.value,
        'feed': feed,
        'liked': liked,
        'likes': feed.likes.all(),
    }
    if request.is_ajax():
        html    = render_to_string('feed/like_section.html', context, request=request)
        return JsonResponse({'form': html})



class FeedDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Feed
    success_url = '/posts'


    def test_func(self):
        feed = self.get_object()
        if self.request.user == feed.author:
            return True
        return False

    


class OpinionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model   = Opinion
    
    def get_success_url(self):
        feed = self.object.feed
        return reverse_lazy('feed-detail', kwargs={'pk': feed.id})
        

    def test_func(self):
        opinion = self.get_object()
        if self.request.user == opinion.user:
            return True
        return False




class ReplyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model   = Opinion

    def get_success_url(self):
        feed = self.object.feed
        return reverse_lazy('feed-detail', kwargs={'pk': feed.id})

    def test_func(self):
        reply = self.get_object()
        if self.request.user == reply.user:
            return True
        return False


