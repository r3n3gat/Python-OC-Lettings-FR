import logging

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Letting

logger = logging.getLogger(__name__)


def index(request: HttpRequest) -> HttpResponse:
    """
    View function for lettings index page.
    """
    logger.info("Lettings index requested")

    lettings_list = Letting.objects.all()

    # Pas de query inutile si DEBUG pas activé
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("Lettings count=%s", lettings_list.count())

    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request: HttpRequest, letting_id: int) -> HttpResponse:
    """
    View function for letting page.
    """
    logger.info("Letting detail requested id=%s", letting_id)

    letting_obj = get_object_or_404(Letting, id=letting_id)

    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("Letting loaded title=%s", letting_obj.title)

    context = {'title': letting_obj.title,
               'address': letting_obj.address,
               }
    return render(request, 'lettings/letting.html', context)
