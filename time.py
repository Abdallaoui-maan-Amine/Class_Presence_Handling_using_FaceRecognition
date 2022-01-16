import time

def GET_TIME():
    Temps= time.time()
    local_time = time.ctime(Temps)
    presence = local_time.split(" ")
    return presence

presence = GET_TIME()
print(presence)
