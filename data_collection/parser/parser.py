"""
Module for parsing data from the GitHub API response.
"""

from models import Repo, Issue, Comment


class Parser:
    """
    Parser class for parsing data from the GitHub API response.

    Attributes:
        params (dict): Parameters for the request.
        token (str): GitHub API token.
        query_path (str): Path to the GraphQL query file.
        scraper: Scraper object for making requests to the GitHub API.
        current_issue: Current issue being processed.
    """

    def __init__(self, params=None, token=None, query_path=None, scraper=None):
        """
        Initialize the parser.

        Args:
            params (dict): Parameters for the request.
            token (str): GitHub API token.
            query_path (str): Path to the GraphQL query file.
            scraper: Scraper object for making requests to the GitHub API.
        """
        self.params: dict = params
        self.token: str = token
        self.query_path: str = query_path
        self.scraper = scraper
        self.current_issue = None

    def __get_data(self):
        """
        Get data from the GitHub API using the scraper.

        Returns:
            dict: JSON response from the API.
        """
        pass

    def parse_repo(self, repo_id, total):
        """
        Parse repository data from the API response.

        Args:
            repo_id (str): ID of the repository.
            total (int): Total number of issues in the repository.

        Returns:
            Repo: Parsed repository object.
        """
        pass

    def get_data_objs(self):
        """
        Get data objects from the API response.

        Returns:
            Tuple[Repo, List[Issue], List[Comment]]: Parsed repository, issues, and comments.
        """
        pass

    def parse_comments_node(self, comments_node, issue_id):
        """
        Parse comments from the comments node.

        Args:
            comments_node (dict): Comments node from the API response.
            issue_id (str): ID of the issue.

        Returns:
            List[Comment]: List of parsed comments.
        """
        pass

    def parse_comments(self, data, issue_id):
        """
        Parse comments from the data.

        Args:
            data (list): List of comment nodes.
            issue_id (str): ID of the issue.

        Returns:
            List[Comment]: List of parsed comments.
        """
        pass

    def parse_issue_node(self, issue_node, repo):
        """
        Parse issues from the issue node.

        Args:
            issue_node (list): List of issue nodes.
            repo (Repo): Repository object.

        Returns:
            Tuple[List[Issue], List[Comment]]: Parsed issues and comments.
        """
        pass

    def parse_issues(self, data, repo):
        """
        Parse issues from the data.

        Args:
            data (dict): Issue data.
            repo (Repo): Repository object.

        Returns:
            Issue: Parsed issue object.
        """
        pass
