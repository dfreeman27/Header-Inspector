import requests
import json 

# GET 1 

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print("=== Response Headers ===")

print(f"\nContent-Type: {response.headers['Content-Type']}")
print(f"Content-Length: {response.headers.get('Content-Length', 'Not specified')}")

cache_control = response.headers.get(
"Cache-Control",
"Not Specified"
)
print(f"Cache-Control:{cache_control}")

rate_limit = response.headers.get("X-RateLimit-Limit", "Not Specified")
print(f"Rate Limit: {rate_limit}")

rate_remaining = response.headers.get("X-RateLimit-Remaining", "Not Specified")
print(f"Responses Remaining: {rate_remaining}")

# GET 2 

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

print("=== Response Headers ===")

print(f"\nContent-Type: {response.headers['Content-Type']}")
print(f"Content-Length: {response.headers.get('Content-Length', 'Not specified')}")

cache_two = response.headers.get(
"Cache-Control",
"Not Specified"
)
print(f"Cache-Control:{cache_two}")

rate_two = response.headers.get("X-RateLimit-Limit", "Not Specified")
print(f"Rate Limit: {rate_two}")

rate_two = response.headers.get("X-RateLimit-Remaining", "Not Specified")
print(f"Responses Remaining: {rate_two}")

# GET 3 

response = requests.get("https://httpbin.org/get")

print("=== Response Headers ===")

print(f"\nContent-Type: {response.headers['Content-Type']}")
print(f"Content-Length: {response.headers.get('Content-Length', 'Not specified')}")

cache_three = response.headers.get(
"Cache-Control",
"Not Specified"
)
print(f"Cache-Control:{cache_three}")

rate_three = response.headers.get("X-RateLimit-Limit", "Not Specified")
print(f"Rate Limit: {rate_three}")

rate_three = response.headers.get("X-RateLimit-Remaining", "Not Specified")
print(f"Responses Remaining: {rate_three}")

# POST

payload = {
    "student": "Dajawaun Freeman",
    "course": "Python",
    "assignment": "HTTP Requests"
}

custom_headers = {
    "X-Student-Name": "Dajawaun Freeman",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

todo = requests.post("https://httpbin.org/post",
json= payload,
headers= custom_headers
)

print("=== Response Headers ===")

print(f"\nContent-Type: {todo.headers['Content-Type']}")
print(f"Content-Length: {todo.headers.get('Content-Length', 'Not specified')}")

new_post = todo.headers.get(
"Cache-Control",
"Not Specified"
)
print(f"Cache-Control:{new_post}")

rate_post = todo.headers.get("X-RateLimit-Limit", "Not Specified")
print(f"Rate Limit: {rate_post}")

post_remain = todo.headers.get("X-RateLimit-Remaining", "Not Specified")
print(f"Responses Remaining: {post_remain}")

print(f"\nResponse Body:")
import json
print(json.dumps(todo.json(), indent=2))