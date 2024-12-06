from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_count = sum(1 for form in self.forms if form.cleaned_data.get("is_main"))
        if is_main_count == 0:
            raise ValidationError("У статьи должен быть один основной тег.")
        if is_main_count > 1:
            raise ValidationError("У статьи не может быть больше одного основного тега.")
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
