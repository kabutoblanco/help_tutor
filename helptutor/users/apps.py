from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    name = 'helptutor.users'
    verbose_name = 'Usuarios'

    # def ready(self):
    #     import users_app.signals
