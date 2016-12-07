from django import forms

from .models import Post, Comment, Member, Meeting,MemberOfMeeting, NumberOfMeeting

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('author', 'text',)

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ('location', 'meeting_date',)
        #widgets = {
        #    'meeting_date': DateInput()
        #}
        #location = forms.CharField()
    #comment = forms.CharField(widget=forms.Textarea)

class NumberOfMeetingForm(forms.ModelForm):
    class Meta:
        model = NumberOfMeeting
        fields = ('meeting_count','total','deposit_member')
    #def __init__(self, *args, **kwargs):
        #super(NumberOfMeetingForm, self).__init__(*args, **kwargs)
        #self.fields['aa'].widget = forms.CheckboxSelectMultiple()


        