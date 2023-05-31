from django.shortcuts import render

from .models import Birthday
from .forms import BirthdayForm
from .utils import calc_birthday_countdown


def birthday(request):
    template_name = 'birthday/birthday.html'
    form = BirthdayForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        form.save()
        birthday_countdown = calc_birthday_countdown(
            form.cleaned_data['birthday']
        )
        context.update({'birthday_countdown': birthday_countdown})
    return render(request, template_name, context)


def birthday_list(request):
    template_name = 'birthday/birthday_list.html'
    birthdays = Birthday.objects.all()
    context = {
        'birthdays': birthdays,
    }
    return render(request, template_name, context)
