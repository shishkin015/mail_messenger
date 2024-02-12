import calendar
from datetime import datetime, timedelta

import pytz
from django.db.models import QuerySet

from messemail.mailings_service.send_mail_and_log import cronjob_send_mail_and_log
from messemail.models import Mailing


def cron_task():
    print('cron_job worked')
    current_time = datetime.now().replace(tzinfo=pytz.UTC)
    current_time_str: str = datetime.now().strftime('%Y-%m-%d %H:%M')
    mailings: QuerySet = Mailing.objects.filter(status='enabled')

    for mailing in mailings:
        next_attempt_str: str = mailing.next_attempt.strftime('%Y-%m-%d %H:%M')
        if next_attempt_str == current_time_str:
            print('email sent')
            cronjob_send_mail_and_log(
                new_mailing=mailing,
                customers=mailing.customers.all(),
                user=mailing.user,
                current_time=datetime.now()
            )
            if mailing.interval == 'every_minute':
                mailing.next_attempt = current_time + timedelta(minutes=1)

            if mailing.interval == 'daily':
                mailing.next_attempt = current_time + timedelta(days=1)

            if mailing.interval == 'weekly':
                mailing.next_attempt = current_time + timedelta(days=7)

            if mailing.interval == 'monthly':
                today = datetime.today()
                days = calendar.monthrange(today.year, today.month)[1]
                mailing.next_attempt = current_time + timedelta(days=days)

            mailing.save()