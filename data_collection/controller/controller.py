from data_collection.scraper import GithubScraper
from data_collection.parser import Parser
from data_collection.loader import Loader
from envconfig import EnvConfig as Config
from typing import Dict, Any, List


class Controller:
    """
    Controller class for managing data loading from GitHub repositories.

    Attributes:
        repos (List[str]): List of repositories to load data from.
        params (Dict[str, Any]): Parameters for data loading.
        config (Config): Configuration object.
        query_path (str): Path to the query.
        token (str): GitHub API token.
    """

    def __init__(self) -> None:
        self.repos: List[str] = [""]
        self.params: Dict[str, Any] = {
            "owner": None,
            "repo": None,
            "cursor": None,
            "counter": 100,
            "issuecursor": None,
            "commcursor": None,
        }
        self.config: Config = Config()
        self.query_path: str = self.config.query_path
        self.token: str = self.config.token

    def __get_next_repo(self) -> bool:
        """
        Get the next repository from the list to load data from.

        Returns:
            bool: True if there are more repositories, False otherwise.
        """
        pass

    def _get_parser(self, scraper: GithubScraper) -> Parser:
        """
        Get a Parser object.

        Args:
            scraper (GithubScraper): Scraper object to be used by the parser.

        Returns:
            Parser: Parser object.
        """
        pass

    def reset_params(self) -> None:
        """Reset parameters for data loading."""
        pass

    def _get_scraper(self) -> GithubScraper:
        """
        Get a GithubScraper object.

        Returns:
            GithubScraper: Scraper object.
        """
        pass

    def _get_loader(self) -> Loader:
        """
        Get a Loader object.

        Returns:
            Loader: Loader object.
        """
        pass

    def __set_params(self, owner: str, repo: str) -> None:
        """
        Set parameters for data loading.

        Args:
            owner (str): Owner of the repository.
            repo (str): Name of the repository.
        """
        pass

    def set_repo_list(self, repo_list: List[str]) -> None:
        """
        Set the list of repositories to load data from.

        Args:
            repo_list (List[str]): List of repositories.
        """
        pass

    def load_data(self, repo_list: List[str]) -> bool:
        """
        Load data from repositories.

        Returns:
            bool: True if data is loaded successfully, False otherwise.
        """
        pass



