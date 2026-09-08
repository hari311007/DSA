class stack:
    def __init__(self,limit=100):
        self.stack_list=[]
        self.limit=limit
    def push(self,value):
        if len(self.stack_list)>=self.limit:
            raise IndexError(f"{value} cannot be added")
        self.stack_list.append(value)
        print("successfully pushed!")
        return True
    def pop(self):
        if not self.stack_list:
            raise IndexError(f"pop cannot be performed!")
        return self.stack_list.pop()
    def print_stack(self):
        for item in reversed(self.stack_list):
            print(item)
        
    def peek(self):
        if not self.stack_list:
            raise IndexError(f"peek cannot be performed!")
        return self.stack_list[-1]
if __name__=="__main__":
    s = stack(limit=2)
    s.push(10) 
    s.push(20)


    try:
      s.push(30) 
      print("Push succeeded!")  


    except IndexError as e:
     print(f"Push failed safely: {e}")

    # The program keeps running normally afterward
    print("Program continues...")
    