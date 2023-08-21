
from django.contrib import admin
from django.urls import path, include
from accounts.views import (register, profile,
                         profile_details, follow, mentors,
                          students, mentor_teacher, 
                          mentor_mentee, student_mentor,
                            UserDeleteView, email_verify)

from django.contrib.auth import views as auth_views
from feed.views import like_feed
from blog.views import about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('verification/', include('verify_email.urls')),
    path('', include('blog.urls')),
    path('notifications/', include('notifications.urls')),
    path('posts/', include('feed.urls')),
    path('information/', include('information.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('like/', like_feed, name='like_feed'),
    path('about_us/', about, name='about'),
    
    #ACCOUNTS URLS
    path('register/', register, name='register'),
    path('account_activation/', email_verify, name='activation'),
    path('profile_edit/', profile, name='profile'),
    path('profile/<str:username>/', profile_details, name='profile_details'),
    path('<str:username>/follow/<option>/', follow, name='follow'),
    #path('tutors/', tutors, name='tutors'),
    path('mentors/', mentors, name='mentors'),
    path('students/', students, name='students'),
    path('mentor_mentee', mentor_mentee, name='mentor_mentee'),
    path('student_mentor', student_mentor, name='student_mentor'),
    path('mentor_teacher', mentor_teacher, name='mentor_teacher'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('<int:pk>/delete/', UserDeleteView.as_view(template_name='accounts/delete_account.html'), name='account_delete'),

    


    #PASSWORD CHANGE
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
        name ='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'),
        name ='password_change'),

    #PASSWORD RESET
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset'),
    path('password_reset_complete/done', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
        name ='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name ='password_reset_confirm'),
    
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
        


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)