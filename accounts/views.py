from .models import *
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import UserRegistrationsForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from blog.models import Post, Follow
from feed.models import Stream, Feed
import json
from .filters import ProfileFilter
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from verify_email.email_handler import send_verification_email



def email_verify(request):
    return render('accounts/email_verify.html')

def register(request):
    if request.method == 'POST':
        form    = UserRegistrationsForm(request.POST)
        if form.is_valid():
            inactive_user = send_verification_email(request, form)
            username    = form.cleaned_data.get('username')
            messages.error(request, f'Almost there! Please check your email Inbox or Spam to verify your account. If you did not receive an email, you may have used an invalid email to register.')
            return redirect('login')

    else:
        form = UserRegistrationsForm()

    return render(request, 'accounts/register.html', {'form': form})



"""
def get_tutors_queryset(query=None):
    queryset    = []
    queries     = query.split(" ")
    for q in queries:
        profiles     = Profile.objects.filter(user__group='Teacher/Tutor').filter(
            Q(Subjects__icontains=q) |
            Q(country__icontains=q) |
            Q(district__icontains=q) |
            Q(township__icontains=q) 
        ).distinct()

        for profile in profiles:
            queryset.append(profile)

    return list(set(queryset))
"""

def get_mentors_queryset(query=None):
    queryset    = []
    queries     = query.split(" ")
    for q in queries:
        profiles     = Profile.objects.filter(user__group='Mentor').filter(
            Q(Subjects__icontains=q) |
            Q(country__icontains=q) 
           
        ).distinct()

        for profile in profiles:
            queryset.append(profile)

    return list(set(queryset))


def get_students_queryset(query=None):
    queryset    = []
    queries     = query.split(" ")
    for q in queries:
        profiles     = Profile.objects.filter(user__group='Student/Mentee').filter(
            Q(Subjects__icontains=q) |
            Q(country__icontains=q) |
            Q(township__icontains=q)|
            Q(institute__icontains=q)
           
        ).distinct()

        for profile in profiles:
            queryset.append(profile)

    return list(set(queryset))




def get_mentor_teacher_queryset(query=None):
    queryset    = []
    queries     = query.split(" ")
    for q in queries:
        profiles     = Profile.objects.filter(user__group='Mentor&Teacher').filter(
            Q(Subjects__icontains=q) |
            Q(country__icontains=q) |
            Q(township__icontains=q)|
            Q(institute__icontains=q)
           
        ).distinct()

        for profile in profiles:
            queryset.append(profile)

    return list(set(queryset))



def get_mentor_student_queryset(query=None):
    queryset    = []
    queries     = query.split(" ")
    for q in queries:
        profiles     = Profile.objects.filter(user__group='Student&Mentor').filter(
            Q(Subjects__icontains=q) |
            Q(country__icontains=q) |
            Q(township__icontains=q)|
            Q(institute__icontains=q)
           
        ).distinct()

        for profile in profiles:
            queryset.append(profile)

    return list(set(queryset))


def get_mentor_mentee_queryset(query=None):
    queryset    = []
    queries     = query.split(" ")
    for q in queries:
        profiles     = Profile.objects.filter(user__group='Mentor&Mentee').filter(
            Q(Subjects__icontains=q) |
            Q(country__icontains=q) |
            Q(township__icontains=q)|
            Q(institute__icontains=q)
           
        ).distinct()

        for profile in profiles:
            queryset.append(profile)

    return list(set(queryset))


"""
def tutors(request):
    context = {}
    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)
        
    profiles = get_tutors_queryset(query)
    context['profiles'] = profiles 


    return render(request, 'accounts/tutors.html', context)
"""

def mentors(request):
    context = {}
    query = ""
    if request.GET:
        query = request.GET['m']
        context['query'] = str(query)
        
    profiles = get_mentors_queryset(query)
    context['profiles'] = profiles 


    return render(request, 'accounts/mentors.html', context)


def students(request):
    context = {}
    query = ""
    if request.GET:
        query = request.GET['s']
        context['query'] = str(query)
        
    profiles = get_students_queryset(query)
    context['profiles'] = profiles 


    return render(request, 'accounts/students.html', context)


def mentor_teacher(request):
    context = {}
    query = ""
    if request.GET:
        query = request.GET['mt']
        context['query'] = str(query)
        
    profiles = get_mentor_teacher_queryset(query)
    context['profiles'] = profiles 


    return render(request, 'accounts/teacher_mentor.html', context)


def mentor_mentee(request):
    context = {}
    query = ""
    if request.GET:
        query = request.GET['mm']
        context['query'] = str(query)
        
    profiles = get_mentor_mentee_queryset(query)
    context['profiles'] = profiles 


    return render(request, 'accounts/mentor_mentee.html', context)


def student_mentor(request):
    context = {}
    query = ""
    if request.GET:
        query = request.GET['sm']
        context['query'] = str(query)
        
    profiles = get_mentor_student_queryset(query)
    context['profiles'] = profiles 


    return render(request, 'accounts/students.html', context)




@login_required
def profile(request):
    username = request.user.username
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f' Your information has been updated!')
            return HttpResponseRedirect(reverse('profile_details', args=[username]))


    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'accounts/profile_edit.html', context)



@login_required
def profile_details(request, username):
    user        = get_object_or_404(MyUser, username=username)
    profile     = Profile.objects.get(user=user)
    posts       = Post.objects.filter(author=user).order_by('-date_posted')
    feeds       = Feed.objects.filter(author=user).order_by('-date_posted')
    following   = Follow.objects.filter(follower=user).all()
    followers   = Follow.objects.filter(following=user).all()

    
    posts_count      = Post.objects.filter(author=user).count() 
    following_count  = Follow.objects.filter(follower=user).count()
    followers_count  = Follow.objects.filter(following=user).count()

    #CHECK FOLLOW STATUS
    follow_status   = Follow.objects.filter(following=user, follower=request.user).exists()
    

    context = {
        'profile': profile,
        'posts': posts,
        'feeds': feeds,
        'following': following,
        'followers': followers,
        'posts_count': posts_count,
        'following_count': following_count,
        'followers_count': followers_count,
        'follow_status': follow_status,
        
    }

    return render(request, 'accounts/profile_detail.html', context) 




def follow(request, username, option):
	user 		= request.user
	following 	= get_object_or_404(MyUser, username=username)

	try:
		f, created 	= Follow.objects.get_or_create(follower=user, following=following)
		if int(option) == 0:
			f.delete()
			Stream.objects.filter(following=following, user=user).all().delete()
		else:
			feeds 	= Feed.objects.all().filter(author=following)

			with transaction.atomic():
				for feed in feeds:
					stream = Stream(feed=feed, user=user, date=feed.date_posted, following=following)
					stream.save()

		return HttpResponseRedirect(reverse('profile_details', args=[username]))

	except user.DoesNotExist:
		return HttpResponseRedirect(reverse('profile_details', args=[username]))





class UserDeleteView(LoginRequiredMixin, DeleteView):

    model = MyUser
    success_url = reverse_lazy('register')

    def test_func(self):
        user = self.get_object()
        if self.request.user == user:
            return True
        return False