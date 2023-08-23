import importlib

from django.apps import AppConfig, apps
from django.conf import settings


class DjangoStaticPublisherConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_static_publisher"

    def ready(self):
        """Populate static patterns"""
        # TODO: Add a more explicit call instead of relying on side effects
        # during import?
        # TODO: Check for mysite.static_publish (sibling to settings?)

        # For each app try to import the static_patterns module which will
        # register them as a side effect.
        for app_config in apps.get_app_configs():
            try:
                importlib.import_module(f"{app_config.module.__name__}.static_publish")
            except ImportError:
                continue
        # Go through each module specified in settings and add those too
        extra_modules = getattr(settings, "STATIC_PUBLISHER_EXTRA_PATTERN_MODULES", [])
        for module_name in extra_modules:
            try:
                importlib.import_module(module_name)
            except ImportError:
                continue

