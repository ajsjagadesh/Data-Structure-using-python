class node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next
        
class linkedlist:
    def __init__(self):
        self.head=None
        
    def insert_top(self,data):     
        n=node(data,self.head)
        self.head = n
       
    def insert_bottom(self,data):
        if(self.head == None):
            n=node(data,self.head)
            self.head = n
        else:
            head1 = self.head
            while(head1 != None):
                 if(head1.next == None):
                     n=node(data,head1.next)
                     head1.next = n
                     return 0
                 else:
                    head1 = head1.next       
                               
                    
    def show(self):
          head = self.head
          while(head != None):
              print(head.data)
              head = head.next
           
           
           
if __name__=="__main__":
    ll = linkedlist()
    ll.insert_top(4)
    ll.insert_bottom(5)
    ll.insert_bottom(11)
    ll.insert_bottom(6)
    ll.insert_top(3)
    ll.insert_bottom(10)
    ll.show()
