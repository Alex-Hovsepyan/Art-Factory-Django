from .models import Header, Home, About, About2, AboutContent, Service, QuestionContainer, Question, ContactInfo
from modeltranslation.translator import register, TranslationOptions

@register(Header)
class HeaderTranslationOptions(TranslationOptions):
    fields = ('path1', 'path2', 'path3', 'path4', 'path5', 'lang1', 'lang2',)

@register(Home)
class HomeTranslationOptions(TranslationOptions):
    fields = ('title1', 'title2', 'text', 'button',)

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'text1', 'colored_part', 'text2', 'text3', 'button',)

@register(About2)
class About2TranslationOptions(TranslationOptions):
    fields = ('title', 'text',)

@register(AboutContent)
class AboutContentTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'button',)

@register(QuestionContainer)
class QuestionContainerTranslationOptions(TranslationOptions):
    fields = ('general_title', 'general_subtitle', 'title', 'text1', 'text2', 'button',)

@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('question', 'text1', 'text2',)

@register(ContactInfo)
class ContactInfoTranslationOptions(TranslationOptions):
    fields = ('button',)