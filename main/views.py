from django.shortcuts import render
from django.core.mail import send_mail
from .forms import AccessForm
from .models import AccessRequest


def access_request_view(request):
    if request.method == 'POST':
        form = AccessForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Сохраняем в базу
            AccessRequest.objects.create(email=email, password=password)

            # Отправляем email (тестово — в консоль)
            send_mail(
                subject='New Access Request',
                message=f'User {email} requested access with password: {password}',
                from_email='noreply@example.com',
                recipient_list=['admin@example.com'],
                fail_silently=True,
            )

            return render(request, 'main/success.html', {'email': email})
    else:
        form = AccessForm()
    return render(request, 'main/access_form.html', {'form': form})
