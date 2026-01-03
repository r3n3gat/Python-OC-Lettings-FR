import logging

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Profile

logger = logging.getLogger(__name__)


def index(request: HttpRequest) -> HttpResponse:
    """
    View function for profiles index page.
    """
    logger.info("Profiles index requested")

    profiles_list = Profile.objects.all()

    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("Profiles count=%s", profiles_list.count())

    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request: HttpRequest, username: str) -> HttpResponse:
    """
    View function for profile page.
    """
    logger.info("Profile detail requested username=%s", username)

    profile_obj = get_object_or_404(Profile, user__username=username)

    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("Profile loaded favorite_city=%s", profile_obj.favorite_city)

    context = {'profile': profile_obj}
    return render(request, 'profiles/profile.html', context)
