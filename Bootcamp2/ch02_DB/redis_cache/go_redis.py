import redis

data = {"Croatia": "Zagreb", "Bahamas": "Nassau"}

r = redis.Redis(host="localhost", port="6379")
r.mset(data)

print(r.get("Bahamas"))

