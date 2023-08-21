from django.shortcuts import render
from .models import Notification

def ShowNotifications(request):
    user            = request.user
    notifications   = Notification.objects.filter(user=user).order_by('-date')
    Notification.objects.filter(user=user, is_seen=False).update(is_seen=True)

    return render(request, 'blog/notifications.html', {'notifications': notifications})


def CountNotifications(request):
    count_notifications     = 0
    if request.user.is_authenticated:
        count_notifications = Notification.objects.filter(user=request.user, is_seen=False).count()

    return {'count_notifications':count_notifications}



