from django.utils import timezone
from django.db import models

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Member(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    kakao = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='uploaded_files/', null=True)
    rank = models.CharField(max_length=20, null=True)
    remark = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Meeting(models.Model):
    location = models.CharField(max_length=100)
    meeting_date = models.DateTimeField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.location

        #return self.objects.select_related('number_meeting').get(id=1)


class NumberOfMeeting(models.Model):
    meeting = models.ForeignKey('blog.Meeting', related_name='number_meeting')
    meeting_count = models.CharField(max_length=20)
    total = models.IntegerField(default=0)
    deposit_member = models.ForeignKey('blog.Member', related_name='deposit_meeting_member', null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.meeting_count

class MemberOfMeeting(models.Model):
    meeting_number = models.ForeignKey('blog.NumberOfMeeting', related_name='member_meeting')
    member = models.ForeignKey('blog.Member', related_name='member')
    amount_yn = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.member.name