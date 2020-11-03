import logging
import requests

from tools.config import cfgfile  # pylint: disable=import-error

logging.basicConfig(
    level=logging.getLevelName(cfgfile.get("core", "verbose"))
    if cfgfile.has_option("core", "verbose")
    else logging.INFO
)
logger = logging.getLogger(__name__)


class ApiRequest:  # pylint: disable=too-few-public-methods
    """
    Provides direct access to api.combahton.net in a simple, yet intuitive way.
    """

    def __init__(self):
        self.email = ""
        self.key = ""

    def request(self, **kwargs):
        """Used to send a request to api.combahton.net with **kwargs"""
        if cfgfile.has_section("user"):
            self.email = cfgfile.get("user", "email")
            self.key = cfgfile.get("user", "key")
        else:
            raise Exception(
                "You haven't added your credentials yet.\nPlease provide your API credentials, use:\n\tcbcli config set user.email <email>\n\tcbcli config set user.key <api-key>"
            )

        post_data = {}
        post_data["email"] = self.email
        post_data["secret"] = self.key
        for key, value in kwargs.items():
            post_data[key] = value

        logger.debug("[Verbose] Follwing data will be sent:")
        for key, value in post_data.items():
            logger.debug("%s == %s", key, value)

        req = requests.post("https://api.combahton.net/v2", json=post_data)
        return req
