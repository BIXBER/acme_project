from django.db import models

from .validators import real_age


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField('Фамилия',
                                 max_length=20,
                                 blank=True,
                                 help_text='Необязательное поле',
                                 )
    birthday = models.DateField('Дата рождения', validators=(real_age,),)
    image = models.ImageField('Фото', upload_to='birthday_images', blank=True)

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )
