from django.db import models

# Create your models here.

class Header(models.Model):

    title = models.CharField('Title', max_length=40)
    path1 = models.CharField('Path 1', max_length=40)
    path2 = models.CharField('Path 2', max_length=40)
    path3= models.CharField('Path 3', max_length=40)
    path4 = models.CharField('Path 4', max_length=40)
    path5 = models.CharField('Path 5', max_length=40)
    lang1 = models.CharField('Language 1', max_length=5)
    lang2 = models.CharField('Language 2', max_length=5)

    class Meta:

        verbose_name = 'Header'
        verbose_name_plural = 'Header'

class Home(models.Model):

    background = models.ImageField('Background')
    title1 = models.CharField('Title 1', max_length=25)
    title2 = models.CharField('Title 2', max_length=25)
    text = models.TextField('Text')
    button = models.CharField('Button', max_length=30)
    img = models.ImageField('Image')

    class Meta:

        verbose_name = 'Home'
        verbose_name_plural = 'Home'

class About(models.Model):

    img = models.ImageField('Image')
    title = models.CharField('Title', max_length=80)
    text1 = models.TextField('Text 1')
    colored_part = models.CharField('Colored Part', max_length=80)
    text2 = models.TextField('Text 2')
    text3 = models.TextField('Text 3')
    button = models.CharField('Button', max_length=30)
    
    class Meta:

        verbose_name = 'About'
        verbose_name_plural = 'About'

class About2(models.Model):

    title = models.CharField('Title', max_length=80)
    text = models.TextField('Text')
    img = models.ImageField('Image')
    
    class Meta:

        verbose_name = 'About 2'
        verbose_name_plural = 'About 2'

class AboutContent(models.Model):

    img = models.ImageField('Image')
    title = models.CharField('Title', max_length=60)
    text = models.TextField('Text')

    def __str__(self) -> str:
        return self.title
    
class Service(models.Model):

    img = models.ImageField('Image')
    title = models.CharField('Title', max_length=40)
    text = models.TextField('Text')
    button = models.CharField('Button', max_length=30)

    def __str__(self) -> str:
        return self.title

class QuestionContainer(models.Model):

    general_title = models.CharField('General Title', max_length=50)
    general_subtitle = models.CharField('General Subtitle', max_length=150)
    title = models.CharField('Title', max_length=80)
    text1 = models.TextField('Text 1')
    text2 = models.TextField('Text 2')
    email = models.EmailField('Email')
    button = models.CharField('Button', max_length=30)

    class Meta:

        verbose_name = 'Question Container'
        verbose_name_plural = 'Question Container'

class Question(models.Model):

    question = models.CharField('Question', max_length=60)
    text1 = models.TextField('Text 1')
    text2 = models.TextField('Text 2')

    def __str__(self) -> str:
        return self.question

class ContactInfo(models.Model):

    google_map = models.TextField('Google Map')
    button = models.CharField('Button', max_length=30)
    social1 = models.URLField('Social 1')
    social2 = models.URLField('Social 2')
    social3 = models.URLField('Social 3')
    social4 = models.URLField('Social 4')
    social5 = models.URLField('Social 5')

    class Meta:

        verbose_name = 'Contact Info'
        verbose_name_plural = 'Contact Info'

class Contact(models.Model):

    username = models.CharField('Username', max_length=60)
    email = models.EmailField('Email')
    message = models.TextField('Message')

    def __str__(self) -> str:
        return f'{self.username} ----------------------------- {self.email}'