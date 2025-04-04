from django.apps import AppConfig


class UserAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_auth'

    # Add signal for user profile creation on front-end.
    def ready(self):
        import user_auth.signals


