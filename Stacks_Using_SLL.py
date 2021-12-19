
class node:              
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next
        

class stack:
    def __init__(self):
        self.head=None
        
    def push(self,data):     
        n=node(data,self.head)
        self.head = n                               
              
    def pop(self):
           if self.head == None:
               print("Stack is Empty No data to Pop out..!")
               return 0
           i = self.head
           self.head = i.next
           print(f"{i.data} is Poping out")
           del i
           
    def show(self):
          head = self.head
          if self.head==None:
              print("Stack is Empty nothing to show..!")
              return 0
          while(head != None):
              print(head.data)
              head = head.next
           
           
if __name__=="__main__":
    s = stack()
    while(True):
        print("\n1> Push")
        print("2> Pop")
        print("3> Show Stack")
        print("4> Exit From Program")
        val = int(input("Enter Your Option :"))
        if val ==  1:
            num = input("Enter Push Value :")
            s.push(num)
            
        elif val == 2:
            s.pop()
         
        elif val == 3:
            print()
            s.show()
            print()
            
        elif val == 4:
            exit("Exiting Program Bye..!")  
 

           