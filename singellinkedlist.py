
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
              
    def delete (self):
           i = self.head
           self.head = i.next
           del i
           
           
           
if __name__=="__main__":
    ll = linkedlist()
    while(True):
        print("\n1> value Insert top")
        print("2> value Insert bottom")
        print("3> Show All values")
        print("4> Delete top value ")
        print("5> Exit From Program")
        val = int(input("Enter Your Option :"))
        if val ==  1:
            num = int(input("Enter top Value :"))
            ll.insert_top(num)
            
        elif val == 2:
            num = int(input("Enter bottom value :"))
            ll.insert_bottom(num)
            
        elif val == 3:
            print()
            print("All Values \n")
            ll.show()
            print()
            
        elif val == 4:
            ll.delete ()
            print("top value deleted\n")
            
        
        elif val == 5:
            exit("Exiting Program Bye..!")  
 
