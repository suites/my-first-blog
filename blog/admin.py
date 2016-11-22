from django.contrib import admin
from .models import Post, Comment, Member, Meeting, NumberOfMeeting, MemberOfMeeting

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Member)
admin.site.register(Meeting)
admin.site.register(NumberOfMeeting)
admin.site.register(MemberOfMeeting)