from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

from model_utils.models import TimeStampedModel


class Area(TimeStampedModel):

    description = models.CharField(
        verbose_name=_('Network area description'),
        help_text=_('Short description of the Network Area.'),
        max_length=100,
        null=True,
        blank=True,
    )
    address = models.PositiveIntegerField(
        verbose_name=_('Network area address'),
        help_text=_('Network area address.'),
        null=False,
        blank=False,
    )

    def __unicode__(self):
        return _(u'Area-{0}').format(self.address)


class System(TimeStampedModel):

    description = models.CharField(
        verbose_name=_('System description'),
        help_text=_('Short description of the Network System.'),
        max_length=100,
        null=True,
        blank=True,
    )
    name = models.CharField(
        verbose_name=_('System name'),
        help_text=_('Unique name of the system in the network.'),
        max_length=50,
        null=False,
        blank=False,
    )
    areas = models.ManyToManyField(Area, blank=True)
    connected_systems = models.ManyToManyField('self', blank=True)

    def __unicode__(self):
        return _(u'System-{0}').format(self.name)

