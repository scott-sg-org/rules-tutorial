def get_things(url):
  requests.get(url)

def post_things(url):
  requests.post(url)

# Try not to match here...
def print_things(thing):
  print(thing)

# Nor here.
def print_two_things(a, b):
  print(a)
  print(b)

def print_and_post_things(url):
  print("thing")
  requests.post(url)
