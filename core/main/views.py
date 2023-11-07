from django.shortcuts import render, redirect
from .models import Header, Home, About, About2, AboutContent, Service, QuestionContainer, Question, ContactInfo, Contact
from .forms import ContactModelForm

# Create your views here.

def index(request):
    header = Header.objects.all()[0]
    home = Home.objects.all()[0]
    about = About.objects.all()[0]
    about2 = About2.objects.all()[0]
    about_content = AboutContent.objects.all()
    services = Service.objects.all()
    question_container = QuestionContainer.objects.all()[0]
    question = Question.objects.all()
    contact_info = ContactInfo.objects.all()[0]

    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return redirect('/')
    else:
        form = ContactModelForm()

    return render(request, 'index.html', context={
        'header':header,
        'home':home,
        'about':about,
        'about2':about2,
        'about_content':about_content,
        'services':services,
        'question_container':question_container,
        'question':question,
        'contact_info':contact_info,
    })