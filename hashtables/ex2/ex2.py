#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    cache={}
    # Your code here
    for ticket in tickets:
        cache[ticket.source] = ticket.destination
    route = []
    origin= cache["NONE"]
    while origin != "NONE":
        route.append(cache[origin])
        origin = cache[origin]
        

    return route
