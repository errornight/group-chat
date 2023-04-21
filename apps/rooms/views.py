from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Group

@login_required
def all_groups(request):
    q = request.GET.get('q')
    if q:
        groups = Group.objects.filter(Q(title__icontains=q) |
                                      Q(description__icontains=q) |
                                      Q(owner__username__icontains=q)).order_by('-date')
    else:
        groups = Group.objects.all()
    context = {'groups': groups}
    return render(request, 'rooms/all-groups.html', context)

@login_required
def group_detail(request, uuid):
    group = get_object_or_404(Group, uuid=uuid)
    if request.GET.get('leave', False):
        group.members.remove(request.user)
        if group.members.count() == 0:  # if a group has no member, WE REMOVE IT.
            group.delete()
        return redirect('AllGroups')
    else:
        group.members.add(request.user)


    if request.method == 'POST':
        if request.POST.get('message', False):
            group.messages.create(sender=request.user,
                                  group=group,
                                  body=request.POST['message'])


    context = {'group': group, 'messages': group.messages.order_by('date')}
    return render(request, 'rooms/group.html', context)

@login_required()
def create_room(request):
    if request.method == 'POST':
        group = Group.objects.create(title=request.POST['title'],
                                     description=request.POST['description'],
                                     owner=request.user)
        return redirect('GroupDetail', group.uuid)
    return render(request, 'rooms/create-room.html')