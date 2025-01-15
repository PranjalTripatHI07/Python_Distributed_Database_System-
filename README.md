# Distributed Database System

A Python implementation of a distributed database system using SQLite and threading for concurrent operations.

## Project Structure

```
├── main.py          # Main application file with thread management
├── models.py        # Data models with validation
├── database.py      # Database operations and connections
└── README.md        # This file
```

## Features

- Concurrent database operations using threading
- Separate SQLite databases for different models
- Application-level data validation
- Thread-safe database operations
- Comprehensive error handling and logging
- Performance metrics tracking

## Models

### Users (users.db)
- id: Integer (Primary Key)
- name: String
- email: String (Unique)

### Products (products.db)
- id: Integer (Primary Key)
- name: String
- price: Float

### Orders (orders.db)
- id: Integer (Primary Key)
- user_id: Integer
- product_id: Integer
- quantity: Integer

## Validation Rules

- All IDs must be positive integers
- Names must be non-empty strings
- Email must follow valid format
- Product prices cannot be negative
- Order quantities must be positive

## Usage

1. Ensure you have Python 3.x installed
2. Clone the repository
3. Run the application:
```bash
python main.py
```

## Expected Output

The program will:
1. Create separate SQLite databases
2. Attempt to insert test data concurrently
3. Log successful and failed operations
4. Display final results from all databases
5. Show performance metrics

## Test Data

The application includes test data with both valid and invalid entries to demonstrate validation:

- Valid entries will be inserted successfully
- Invalid entries will fail with appropriate error messages:
  - Duplicate emails
  - Negative prices
  - Invalid quantities
  - Non-existent references

## Performance Metrics

The application measures and reports:
- Thread execution time
- Total execution time
- Individual operation success/failure

## Dependencies

- Python 3.x
- SQLite3 (included in Python standard library)
- threading (included in Python standard library)
- logging (included in Python standard library)

## Error Handling

The system handles various error scenarios:
- Database connection errors
- Validation failures
- Concurrent operation conflicts
- Data integrity violations

## Logging

Comprehensive logging includes:
- Operation success/failure
- Validation errors
- Database operation results
- Performance metrics

## Threading

- Each insertion operation runs in a separate thread
- Thread synchronization using locks
- Concurrent execution of all operations
- Safe database access across threads
