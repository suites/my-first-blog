from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum, Count, Avg
from .models import Post, Comment, Member, Meeting, NumberOfMeeting, MemberOfMeeting
from .forms import PostForm, CommentForm


def home(request):
    return render(request, 'blog/home.html')

def members(request):
    members = Member.objects.all().order_by('rank')
    return render(request, 'blog/members.html', {'members': members})

def photos(request):
    return render(request, 'blog/photos.html')

def meeting_list(request):
    meetings = Meeting.objects.values(  
        'id','location','meeting_date'
    ).annotate(
        daily_total=Sum('number_meeting__total'),
        meeting_count=Count('number_meeting__id')
    )
    return render(request, 'blog/meeting_list.html', {'meetings': meetings})

def meeting_detail(request, pk):
    meeting_model = get_object_or_404(Meeting, pk=pk)
    meeting = meeting_model.number_meeting.values(  
        'id', 'meeting_count','total', 'deposit_member__name'
    ).annotate(
        member_count=Count('member_meeting__id'),
        division=F('total') / Count('member_meeting__id')
    )
    member_meeting = meeting_model.number_meeting.values(  
        'id','meeting_count', 'member_meeting__member__name'
    )
    return render(request, 'blog/meeting_detail.html', {'meeting': meeting, 'meeting_model': meeting_model, 'member_meeting': member_meeting})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})



@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)