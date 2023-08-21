import importlib

from django.apps import AppConfig, apps


class DjangoStaticPublisherConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_static_publisher"

    def ready(self):
        """Populate static patterns"""
        # TODO: Allow settings to point to more static_publish locations
        # TODO: Check for mysite.static_publish (sibling to settings?)
        for app_config in apps.get_app_configs():
            # For each app try to import the static_patterns module
            # which will register them as a side effect
            try:
                importlib.import_module(f"{app_config.module.__name__}.static_publish")
            except ImportError:
                continue
