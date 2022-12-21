from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Employee, FeedBack, Contact, Spam


class NewsEmployee(admin.ModelAdmin):
    list = ['instagram', 'facebook', 'name', 'img']

    def image(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='100' height='110'")


class NewsFeedBack(admin.ModelAdmin):
    list = ['img', 'text']

    def image_(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='100' height='110'")


class NewsContact(admin.ModelAdmin):
    list = ['name', 'phone', 'email', 'message']

    def name(self, obj):
        return mark_safe(f"<name src={obj.name.url}")


class NewsSpam(admin.ModelAdmin):
    list = ['email']

    def email(self, obj):
        return mark_safe(f"<email src={obj.email.url}")


admin.site.register(Employee, NewsEmployee)
admin.site.register(FeedBack, NewsFeedBack)
admin.site.register(Contact, NewsContact)
admin.site.register(Spam, NewsSpam)
