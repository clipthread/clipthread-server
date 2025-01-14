# ClipThread Server

ClipThread is a FastAPI application designed to synchronize clipboard data between different machines. It provides endpoints for managing clipboard entries and journal entries, allowing users to fetch and add data seamlessly.

## Features

- Synchronize clipboard data across devices.
- Add, fetch, update, and delete journal entries.
- Easy-to-use API with FastAPI.

## Project Structure

```
clipthread-server
├── src
│   ├── api
│   │   ├── __init__.py
│   │   ├── clipboard.py
│   │   └── journal.py
│   ├── core
│   │   ├── __init__.py
│   │   └── config.py
│   ├── db
│   │   ├── __init__.py
│   │   └── handlers.py
│   ├── models
│   │   ├── __init__.py
│   │   └── schemas.py
│   └── main.py
├── tests
│   ├── __init__.py
│   ├── test_clipboard.py
│   └── test_journal.py
├── requirements.txt
├── .env
└── README.md
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd clipthread-server
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables in the `.env` file.

## Usage

To run the application, execute:

```bash
uvicorn src.main:app --reload
```

Visit `http://localhost:8000/docs` to access the interactive API documentation.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.