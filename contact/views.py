from django.shortcuts import render
from .models import ContactDataTwo
from .forms import ContactForm
from django.core.mail import send_mail

app_name = 'contact'

# Create your views here.
def Contact_view(request):
    contact = ContactDataTwo.objects.all()
    form = ContactForm()
    sended = 'False'
    get_email = 'no'

    if request.method == "POST":
        form = ContactForm(request.POST)
        get_email = request.POST.get('email','null')
        get_message = request.POST.get('text','no text')
        date = request.POST.get('date', 'null')
        schedule = request.POST.get('schedule','null')
        service = request.POST.get('service','null')
        service_pack = request.POST.get('service_pack','null')

        reply = ("Thank you for your contact, our meeting is scheduled for " + date +
                " " + schedule + "\n Please click on the following link to attend to the meeting when it's time :) \n"
                + "https://whereby.com/potatonetworks?utm_source=onboarding&utm_content=link")
        title = service_pack + " " + date
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            send_mail(title,
            reply,
            'jhonnykellerdev@gmail.com',
            [get_email],
            fail_silently=False)
            send_mail(get_email,
            get_message,
            'jhonnykellerdev@gmail.com',
            ['jhonnykellerdev@gmail.com'],
            fail_silently=False)
            sended = 'True'


    return render(request, 'contact/contact.html', {'contact':contact,'form':form,'sended':sended,'get_email':get_email})
