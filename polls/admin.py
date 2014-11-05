from django.contrib import admin
from polls.models import Question,Choice

# Register your models here.

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    fieldsets = [
        ('Texte de la question : ', {'fields': ['question_text']}),
        ('Date information',        {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)


