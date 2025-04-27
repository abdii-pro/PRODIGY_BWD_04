# Flask Redis Caching Example

This is a simple Flask application that demonstrates caching with Redis to optimize performance and reduce redundant database calls. It includes endpoints to fetch, update, and delete users with caching and cache invalidation.

## Features

- **Caching with Redis**: Caches user data for 60 seconds to improve response time.
- **Cache Invalidation**: Updates or deletes users invalidate the cache to ensure data consistency.
- **Simulated Database**: Uses hardcoded data to simulate database calls.

## Requirements

- Python 3.6+
- Flask
- Flask-Caching
- Redis (make sure Redis server is running)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Make sure Redis is installed and running on your local machine or use a Redis cloud service:
   ```bash
   redis-server
   ```

## Usage

1. Run the Flask app:
   ```bash
   python app.py
   ```

2. Open your browser or use Postman to interact with the following endpoints:
   - **GET /users**: Fetch the list of users (cached for 60 seconds).
   - **POST /update_user/<user_id>**: Simulate updating a user and invalidate cache.
   - **DELETE /delete_user/<user_id>**: Simulate deleting a user and invalidate cache.

## Example Requests

1. **Fetch users**:
   ```bash
   GET http://localhost:5000/users
   ```

2. **Update user**:
   ```bash
   POST http://localhost:5000/update_user/1
   ```

3. **Delete user**:
   ```bash
   DELETE http://localhost:5000/delete_user/1
   ```

## Notes

- The app uses Redis for caching. Make sure Redis is set up and accessible on the URL configured (`redis://localhost:6379/0`).
- This is a simple example, so the database is simulated. Replace the hardcoded data with real database calls in a production app.
