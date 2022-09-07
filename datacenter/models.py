from django.db import models
from django.utils import timezone
from datetime import timedelta


def format_duration(duration):
    duration_in_seconds = duration.total_seconds()
    hours = int(duration_in_seconds // 3600)
    minutes = int((duration_in_seconds % 3600) // 60)
    if not hours:
        return f'{minutes}мин.'
    else:
        return f'{hours}ч. {minutes}мин.'


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        entry_time = timezone.localtime(self.entered_at)
        leave_time = timezone.localtime(self.leaved_at)
        if not leave_time:
            current_time = timezone.localtime().replace(microsecond=0)
            return current_time - entry_time
        else:
            return leave_time - entry_time

    def is_strange(self, minutes=60):
        suspicious_delta = timedelta(minutes=minutes)
        return self.get_duration() > suspicious_delta
