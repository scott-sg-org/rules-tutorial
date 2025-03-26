import logging as lg

def get_user(uid):
    d = {1: "harry", 2: "ron", 3: "hermione"}
    return d[uid]

# Match both of these using an ellipsis.
logging.info(get_user(1)
    + " logged in")
lg.info(get_user(2)
    + " logged in")
