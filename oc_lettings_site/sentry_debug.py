import logging

logger = logging.getLogger(__name__)


def trigger_error(request):
    # WARNING (pas ERROR) pour éviter de créer un event Sentry via LoggingIntegration
    logger.warning("Sentry debug endpoint called - forcing ZeroDivisionError")
    1 / 0
