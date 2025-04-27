from flask import Flask, jsonify
from flask_caching import Cache
import redis
import time

app = Flask(__name__)

# Configure Redis cache
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_REDIS_URL'] = "redis://localhost:6379/0"  # Adjust based on your Redis setup

cache = Cache(app)

# Example endpoint to fetch users
@app.route('/users')
@cache.cached(timeout=60, key_prefix='users')  # Cache for 60 seconds
def get_users():
    start_time = time.time()
    
    # Simulating a database call (replace this with actual DB calls in real-world apps)
    users = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"},
    ]
    
    end_time = time.time()
    print(f"Response Time: {end_time - start_time} seconds")
    
    return jsonify(users)

# Example endpoint to update a user and invalidate cache
@app.route('/update_user/<int:user_id>', methods=['POST'])
def update_user(user_id):
    # Simulate updating the user in the database (not implemented in this example)
    cache.delete('users')  # Invalidate cache for 'users' endpoint
    return jsonify({"message": "User updated successfully"}), 200

# Example endpoint to delete a user and invalidate cache
@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Simulate deleting the user in the database (not implemented in this example)
    cache.delete('users')  # Invalidate cache for 'users' endpoint
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
