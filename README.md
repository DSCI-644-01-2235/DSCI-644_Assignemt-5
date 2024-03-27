# Assignment # 5: Building the Data Collection Pipeline

## Overview:

In this assignment, you will build a comprehensive data collection pipeline for fetching GitHub repository details, issues, and comments. The pipeline should include a scraper module that interacts with the GitHub GraphQL API, a parser module to process the obtained JSON data, a database handler for database interactions, a loader to validate and perform CRUD operations, and a controller to orchestrate the entire data flow. The components will be coordinated through a command-line interface (CLI) using the Click package.

- **Scraper Module:** Utilizes a GraphQL file, GitHub token, and Faker agent to retrieve a repository's issues and comments from the GitHub GraphQL API. Pagination handling and error management are essential components of the scraper.

- **Parser Module:** Parses the JSON data obtained by the scraper, preparing it for insertion or updating into the database. Two separate classes, `parser.py` and `loader.py`, handle data parsing and validation/insertion operations.

- **Database Configuration and Modeling:** Configures the database and defines SQLAlchemy models for repository information, issues, and comments. Alembic is used for database schema management.

- **Database Handler:** Implements functions in `handler.py` for interacting with the database, including CRUD operations, optimized bulk inserts, and data validation before insertion.

- **Loader Module:** Handles the validation of parsed data and performs CRUD operations. It ensures that data is correctly processed before updating the database.

- **Controller Module:** Orchestrates the data pipeline by integrating the scraper, parser, loader, and database handler. Ensures a smooth data flow and handles exceptions.

- **CLI Module:** Provides a command-line interface through `cli_handler.py`, allowing users to specify repositories and the data they want to retrieve. Utilizes the controller to fetch and process data.

## Task 1: Scraper Module 

**Objective:** Create a scraper to fetch data from GitHub repositories.

1. **Boilerplate Code:** Start with the boilerplate code provided in `data_collection/scraper/scraper.py`. This file contains the basic structure and function prototypes.

2. **Dependencies:** Install the required dependencies using the following commands:
   ```bash
    pip install -r requirements.txt
   ```

3. **GitHub Token:** Use the GitHub token obtained in the previous assignment. Add it to your environment variables or use a `.env` file. Refer to the `.env.template` file for guidance.

4. **GraphQL Query:** Use the GraphQL query file from the provided in the query file by reading it into scraper.py and then passing it while makeing the request to fetch repository details, issues, and comments.

5. **User Agent:** Understand the purpose of the user agent and its utility in the `__set_headers` function. 
Visit [this article](https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/) for more information on user agents.
Also refer to the following code snippet for the user agent format:

   ```python
   def __set_headers(self):
        self.headers = {
            "Authorization": f"bearer {self.token}",
            "User-Agent": "YOUR_USER_AGENT"
        }
    ```

Additionally, you can check this [link](https://scrapeops.io/python-web-scraping-playbook/python-fake-user-agents/) to learn how to generate a user agent using the `faker_agent` library.

6. **Error Handling:** Implement error handling for network issues and GitHub rate limits issues. Check out the github documentation for [rate limits and info on status codes](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting)

7. **Pagination:** Handle pagination using GraphQL cursors to fetch additional data. Make use of the cursors GitHub provides to fetch all the data. You can refer to pagination.ipynb file for more information on how to handle pagination. This file gives a small working demo of how to handle pagination using GraphQL cursors. Use the logic as a reference and implement it in the scraper. 


8. **Return Format:** Ensure that the scraper returns all the fetched data in a dictionary format.

## Task 2: Database Configuration and Modeling 

**Objective:** Configure the database, define models, and use Alembic for schema management.

1. **Boilerplate Code:** Start with the boilerplate code in `database/handler.py` for handling database configuration.
Visit [this link](https://docs.sqlalchemy.org/en/14/core/engines.html) for more information on database engines.
Visit [this link](https://coderpad.io/blog/development/sqlalchemy-with-postgresql/) for more information on how to connect to a PostgreSQL database using SQLAlchemy.

2. **Modeling:** Design a relational database schema for storing repository information, issues, and comments.
2. **CRUD Operations:** Include functions for inserting, updating, and querying data. As an added goal utilize bulk insert methods for optimized data insertion.

3. **Optimized Insert:** Utilize bulk insert methods for optimized data insertion.


4. **Alembic Migration:** Implement Alembic for database schema management. Refer to the provided [link](https://medium.com/@johnidouglasmarangon/using-migrations-in-python-sqlalchemy-with-alembic-docker-solution-bd79b219d6a) for guidance on using SQLAlchemy and Alembic together.

To learn more about ORMs : https://www.fullstackpython.com/object-relational-mappers-orms.html 

Alembic helps you in creating migrations for your database. Once you have your models defined, you can use alembic to create migrations for your database. Make sure to import the models in the alembic env.py file.


## Task 3: Parser Module 

**Objective:** Create parsers to process the data acquired from the scraper.

1. **Boilerplate Code:** Use the boilerplate code in `data_collection/parser/parser.py` as a foundation.

2. **Parser Implementation:** Implement parsers for repositories, issues, and comments.

3. **Pagination Handling:** Handle pagination using GraphQL cursors to fetch additional data. Make use of the cursors GitHub provides to fetch all the data. The parser should obtain the next cursor from the current scrapped data and pass it to the scraper to fetch the next page of data.

4. **Data Preparation:** Prepare the parsed data for insertion into the database. Lot of time you don't need all the data that you have scrapped. You can use the parsed data to create a dictionary with only the required data and pass it to the loader. Also make sure to handle the data types of the data that you are passing to the loader. 

## Task 4: Loader Module 

**Objective:** Create a loader to validate parsed data and perform CRUD operations.

1. **Boilerplate Code:** Use the boilerplate code in `data_collection/loader/loader.py` as a foundation.

2. **Loader Implementation:** Implement the loader to handle data validation and perform CRUD operations.

3. **Error Handling:** Implement error handling to manage issues during data loading.

## Task 5: Controller Module 

**Objective:** Build a controller to orchestrate the data pipeline.

1. **Controller Class:** Create a `Controller` class in `data_collection/controller/main.py`.

2. **Integration:** Integrate the scraper, parser, loader, and database handler into the controller.

3. **Data Flow:** Fetch data, parse it, validate it using the loader, and pass it to the database handler. The controller is for orchestrating the data pipeline and should not contain business logic.

4. **Exception Handling:** Handle exceptions and ensure a smooth data flow.

## Task 6: CLI Module 

**Objective:** Build a command-line interface for your data pipeline.

1. **CLI Handler:** Create a CLI handler in `data_collection/cli_handler.py`.

2. **CLI Command:** Implement a CLI command that accepts a list of repository names or a file with a list of repositories as input.

3. **Controller Integration:** Use the controller to fetch data for the specified repositories.

4. **Options:** Provide options for users to specify the data they want to retrieve.

## Task 7: Testing 

**Objective:** Write unit tests for your code.

1. **Unit Tests:** Write unit tests for the scraper, parser, loader, database handler, and controller.

2. **Mocking:** Mock the GraphQL API calls, database interactions, and loader operations in your tests.

3. **Code Coverage:** Ensure that the tests cover all code paths and handle exceptions.

4. **Test Framework:** Use the `pytest` framework to run the tests.

## Task 8: Dockerize 

**Objective:** Dockerize your application.

1. **Dockerfile:** Create a `Dockerfile` to build your application. Refer to [this link](https://docs.docker.com/language/python/build-images/) for guidance on creating a Dockerfile for Python applications.

2. **docker-compose:** Use `docker-compose` to run your application. Refer to [this link](https://docs.docker.com/compose/) for guidance on using Docker Compose.

3. **Container Testing:** Ensure that the application runs without any issues in the container.

4. **Reference:** Use the `docker-compose.yml` file provided in the boilerplate code as a reference.

## Task 9: Software Quality :

**Objective:** Ensure that your code adheres to best practices and is well-organized.

1. **Pylint:** Use Pylint to lint your code and ensure that it adheres to PEP 8 standards. Aim for a score of 8 or higher.

2. **Black:** Use Black to format your code and ensure that it adheres to PEP 8 standards.

## Expected Outcome :

Upon completion of this assignment, you should have a well-tested and functioning project. When provided with a username/repo and token via the CLI, the application should update the database with relevant information on the repository, its issues, and comments. The implementation should adhere to best practices, handle errors gracefully, and demonstrate proficiency in data collection, parsing, and database interaction using a modular and organized code structure. If you have any questions or need further clarification on specific concepts, feel free to ask. Good luck with your assignment!
