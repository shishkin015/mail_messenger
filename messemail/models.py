from django.db import models

NULLABLE = {
    'blank': True, 'null': True
}


class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='имя')
    email = models.EmailField(max_length=150, unique=True, verbose_name='почта')
    comment = models.TextField(**NULLABLE, verbose_name='комментарий')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.email})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Message(models.Model):
    email = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='почта')

    title = models.CharField(max_length=150, verbose_name='тема письма')
    text = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class MailingSetup(models.Model):
    DAILY = "Раз в день"
    WEEKLY = "Раз в неделю"
    MONTHLY = "Раз в месяц"

    PERIODICITY_CHOICES = [
        (DAILY, "Раз в день"),
        (WEEKLY, "Раз в неделю"),
        (MONTHLY, "Раз в месяц"),
    ]

    CREATED = 'Создана'
    STARTED = 'Запущена'
    COMPLETED = 'Завершена'

    STATUS_CHOICES = [
        (COMPLETED, "Завершена"),
        (CREATED, "Создана"),
        (STARTED, "Запущена"),
    ]

    email = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='почта')
    title = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='тема письма')

    mailing_time = models.TimeField(verbose_name='время рассылки')
    periodicity = models.CharField(max_length=50, choices=PERIODICITY_CHOICES, verbose_name='периодичность')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=CREATED, verbose_name='статус')

    def __str__(self):
        return f'{self.email} {self.mailing_time} {self.periodicity} {self.status}'

    class Meta:
        verbose_name = 'настройка рассылки'
        verbose_name_plural = 'настройка рассылки'


