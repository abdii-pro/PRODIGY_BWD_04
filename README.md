# PRODIGY_BWD_04
This Flask app uses Redis for caching to optimize performance. The /users endpoint fetches a list of users, caching the result for 60 seconds. The /update_user and /delete_user endpoints simulate user updates and deletions, clearing the cache to ensure data consistency.
