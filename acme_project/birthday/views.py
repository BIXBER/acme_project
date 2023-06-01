from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator

from .models import Birthday
from .forms import BirthdayForm
from .utils import calc_birthday_countdown


def birthday(request, pk=None):
    template_name = 'birthday/birthday.html'
    if pk is not None:
        instance = get_object_or_404(Birthday, pk=pk)
    else:
        instance = None
    form = BirthdayForm(
        request.POST or None,
        files=request.FILES or None,
        instance=instance)
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
    birthdays = Birthday.objects.order_by('id')

    paginator = Paginator(birthdays, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, template_name, context)


def delete_birthday(request, pk):
    template_name = 'birthday/birthday.html'
    instance = get_object_or_404(Birthday, pk=pk)
    form = BirthdayForm(instance=instance)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        instance.delete()
        return redirect('birthday:list')
    return render(request, template_name, context)
