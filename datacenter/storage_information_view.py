from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
from datacenter.models import format_duration


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in active_visits:
        person_name = visit.passcard.owner_name
        duration = visit.get_duration()
        non_closed_visits.append(
            {
                'who_entered': person_name,
                'entered_at': timezone.localtime(visit.entered_at),
                'duration': format_duration(duration),
                'is_strange': visit.is_strange(),
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
