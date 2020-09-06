from django.shortcuts import render,redirect
from django.contrib.auth.views import login_required
from watch.models import Comments,profile,CommentLike,Videos,Reply
# Create your views here.

@login_required
def delete_comments(request,id):
    comment = Comments.objects.get(id=id,user=request.user)
    video = Videos.objects.get(id=comment.video.id)
    comment.delete()
    return redirect('/watch/{0}'.format(video.id))

@login_required
def delete_video(request,id):
    video = Videos.objects.get(id=id,user=request.user)
    video.delete()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def delete_reply(request,id):
    reply = Reply.objects.get(id=id,user=request.user)
    reply.delete()
    return redirect(request.META.get('HTTP_REFERER'))