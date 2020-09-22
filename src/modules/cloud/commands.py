import click

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)

@click.group()
def cloud():
    """cloud server management module"""
    pass