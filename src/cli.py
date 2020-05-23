#!/usr/bin/env python3

from argparse import Action, ArgumentParser

class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination= values
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = ArgumentParser(description="""
    Back up PostgresSQL databases locally or to AWS S3.
    """)

    parser.add_argument("url", help="URL of the atabase to backup")
    parser.add_argument("--driver",
            help="how & where to store backup",
            nargs=2, # Number of arguments
            action=DriverAction,
            required=True)
    
    return parser
