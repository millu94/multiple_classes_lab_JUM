class BusStop:
    def __init__(self,name):
        self.name=name
        self.queue=[]

    def add_to_queue(self,name):
        self.queue.append(name)
    
    def clear():
        self.queue=[]

    def queue_length():
        return len(self.queue)
    
    