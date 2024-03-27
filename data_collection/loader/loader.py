"""
Module for loading data objects into the database.
"""

from database.handler import DatabaseHandler
from envconfig import EnvConfig


class Loader:
    """
    Class for loading data objects into the database.

    Attributes:
        config (Config): Configuration object.
        db_handler (DatabaseHandler): Database handler object.
    """

    def __init__(self) -> None:
        """
        Initialize the Loader.

        Creates a DatabaseHandler instance using configuration settings.
        """
        self.envconfig: EnvConfig = None
        db_url = None
        self.db_handler = None

    def get_db_url(self) -> str:
        """
        Get the database URL.

        Returns:
            str: Database URL.
        """
        pass

    def load_objs(self, objs: list) -> bool:
        """
        Load a list of objects into the database.

        Args:
            objs (list): List of objects to load.

        Returns:
            bool: True if objects are loaded successfully, False otherwise.
        """
        pass


    def load_obj(self, obj) -> bool:
        """
        Load a single object into the database.

        Args:
            obj: Object to load.

        Returns:
            bool: True if object is loaded successfully, False otherwise.
        """
        pass

