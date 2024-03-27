## This file is the handler for the CLI. It is responsible for parsing the command line arguments and calling the appropriate functions from the scraper and issue_parser modules. It is also responsible for printing the output to the console.
'''
This file is the handler for the CLI. 
It is responsible for parsing the command line arguments and calling the appropriate functions from the scraper and issue_parser modules. 
It is also responsible for printing the output to the console.
'''

import click
from data_collection.controller import Controller

controller = Controller()

@click.group()
def scraper():
    """
    CLI for scraping data from GitHub.
    """
    pass

@scraper.command()
@click.option("-f", "--file", type=click.File("r"), help="File containing repo names")
def start(file):
    """
    Start the data scraping pipeline.
    """
    repo_names = [line.strip() for line in file.readlines()]
    controller.load_data(repo_names)

if __name__ == "__main__":
    scraper()
