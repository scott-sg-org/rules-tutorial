import logging

def get_user(uid):
    d = {1: "harry", 2: "ron", 3: "hermione"}
    return d[uid]

# Try matching these two cases by editing the pattern to match any string.
logging.info(get_user(1)
    + " flew in")
logging.info(get_user(2)
    + " apparated in")
#train = " arrived by train"
logging.info(get_user(3)
    + train)
