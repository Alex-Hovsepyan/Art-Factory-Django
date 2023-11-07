from django.contrib import admin
from .models import Header, Home, About, About2, AboutContent, Service, QuestionContainer, Question, ContactInfo, Contact
from modeltranslation.admin import TranslationAdmin
# Register your models here.

class HeaderAdmin(TranslationAdmin): 
    pass

class HomeAdmin(TranslationAdmin): 
    pass

class AboutAdmin(TranslationAdmin): 
    pass

class About2Admin(TranslationAdmin): 
    pass

class AboutContentAdmin(TranslationAdmin): 
    pass

class ServiceAdmin(TranslationAdmin): 
    pass

class QuestionContainerAdmin(TranslationAdmin): 
    pass

class QuestionAdmin(TranslationAdmin): 
    pass

class ContactInfoAdmin(TranslationAdmin): 
    pass

admin.site.register(Header)
admin.site.register(Home)
admin.site.register(About)
admin.site.register(About2)
admin.site.register(AboutContent)
admin.site.register(Service)
admin.site.register(QuestionContainer)
admin.site.register(Question)
admin.site.register(ContactInfo)
admin.site.register(Contact)