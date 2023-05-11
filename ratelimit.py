import time

# Define a rate limiter function that takes a maximum number of requests and time interval
def rate_limiter(max_requests, interval):
    # Initialize a request counter and timestamp
    counter = 0
    timestamp = time.time()

    # Define a decorator that wraps around the API function
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Get the current time
            now = time.time()

            # If the time interval has passed, reset the counter and timestamp
            if now - timestamp > interval:
                counter = 0
                timestamp = now

            # If the maximum number of requests has been reached, return an error response
            if counter >= max_requests:
                return "Rate limit exceeded"

            # Increment the request counter and call the API function
            counter += 1
            return func(*args, **kwargs)

        return wrapper

    return decorator
