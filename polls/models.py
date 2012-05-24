from django.db import models
from django.contrib import admin

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __unicode__(self):
        return self.choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 5

class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date')
    search_fields = ('question', 'pub_date')
    date_hierarchy = 'pub_date'
    list_filter = ('pub_date',)
    ordering = ('-pub_date', )
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)