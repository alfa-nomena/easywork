from django.contrib import admin

from .models import Candidate, Skill


class SkillInline(admin.TabularInline):
    '''Tabular Inline View for Skill'''

    model = Skill
    extra = 1
    
class CandidateAdmin(admin.ModelAdmin):
    inlines = [SkillInline]    

admin.site.register(Candidate, CandidateAdmin)
