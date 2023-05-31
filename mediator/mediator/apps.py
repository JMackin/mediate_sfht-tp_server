from django.apps import AppConfig as ac, AppConfig

from sftp_machine import portals


class MediatorConfig(AppConfig):
    AppConfig.name = "mediator"
    AppConfig.path = "mediator/wsgi"
class SftpMachineConfig(AppConfig):

    AppConfig.name = "sftp_machine"

    def ready(self):
        mainportal = portals.SftpPortal()

class ScrtsConfig(AppConfig):
    AppConfig.name = "secret_things"
    AppConfig.path = "mediator/scrts/secret_things"

class PlacesConfig(AppConfig):
    AppConfig.name = "places_things"
    AppConfig.path = "mediator/places/place_things"
