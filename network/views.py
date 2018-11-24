import logging

from django.shortcuts import render
from django.views.decorators.http import require_GET


LOGGER = logging.getLogger(__name__)


@require_GET
def index(request):
    """
    Main homepage view.
    """
    context = {
        # 'site': Site.objects.get_current()
    }

    return render(request, 'dashboard.html', context)
