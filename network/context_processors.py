from django.conf import settings
from django.contrib.sites.models import Site


def site_processor(request):
    # provide site object across all project
    return {
        'site': Site.objects.get_current(),
        'settings': settings,
    }
