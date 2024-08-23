# The FastAPI project for Ziptie Recruitment Task

### Steps

1. **Clone the repository**

```bash
git clone https://github.com/EliteNinja07/ziptie.git
cd ziptie
```

2. **Create and active a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  
# On Windows use `venv\Scripts\activate`
```

3. **Install the required dependencies**

```bash
pip install -r requirements.txt
```

4. **Rename the .env file**

Please rename the `.env.example` file to `.env`

5. **Running the application**

```bash
fastapi dev app
```

### API Endpoints

### 1. Create an Author

- **Endpoint**: `POST /author`
- **Description**: Creates a new author in the database.
- **Request Body**:
    ```json
    {
        "Name": "Author Name",
        "BirthDate": "YYYY-MM-DD",
        "Country": "Country Name",
        "Email": "author@example.com"
    }
- **Response Body**: Returns the newly created author object with a unique `AuthorID`.

    ```json
    {
        "AuthorID": 1,
        "Name": "Author Name",
        "BirthDate": "YYYY-MM-DD",
        "Country": "Country Name",
        "Email": "author@example.com"
    }
    ```
### 2. Create a Book

- **Endpoint**: `POST /book`
- **Description**: Creates a new book in the database, associated with an existing author.
- **Request Body**:

    ```json
    {
        "Title": "Book Title",
        "Genre": "Genre",
        "PublicationYear": 2023,
        "AuthorID": 1
    }
    ```
- **Response Body**: Returns the newly created book object with a unique `BookID`.
    ```json
    {
        "BookID": 1,
        "Title": "Book Title",
        "Genre": "Genre",
        "PublicationYear": 2023,
        "AuthorID": 1
    }
    ```

### 3. List Books with Author Information

- **Endpoint**: `GET /book/list/`
- **Description**: Creates a new book in the database, associated with an existing author.
- **Query Parameters**:
    - skip: Number of records to skip for pagination (default: 0).
    - limit: Maximum number of records to return (default: 10).
- **Response Body**:
    ```json
    [
        {
            "BookID": 1,
            "Title": "Book Title",
            "Genre": "Genre",
            "PublicationYear": 2023,
            "author": {
            "AuthorID": 1,
            "Name": "Author Name",
            "BirthDate": "YYYY-MM-DD",
            "Country": "Country Name",
            "Email": "author@example.com"
            }
        }
    ]
    ```

