from encodings import utf_8
import os
os.chdir('Files location')
class Store():
      def __init__(self,name): #storing name
          self.name=name    
      def book_selection(self): #function for book selection
          val = int(input("Select any book form the following options : \n\nl Elon Musk \n2 Ratan Tata \n3 Swami Vivekananda"))  
          if val == 1:
            fo= open("em.txt", "r",encoding="utf_8")
            data = fo.read()
            fo.close()
            
          elif val==2:
            fo = open("rt.txt", "r",encoding="utf_8")
            data=fo.read()
            fo.close()
            
          elif val == 3:
             fo=open("sv.txt","r",encoding="utf_8")
             data = fo.read()
             fo.close()
             
          else:
             print('Invalid')
          return data

      def keyword_search(self,data): #keyword search function
            response = input("\n\nDo you know any last keyowrd to jump on (y/Y) for yes (n/N) to start from beginning : ")
            if response =='y' or response == 'Y':
               key = input("\nEnter the keyword : ")
               print()
               n=len(data)
               k = len(key)
      
               flag = False
               while True:
                  for i in range(n):
                      if data[i:i+k].lower() == key.lower():
                           print(data[i:i+200])
                           resl = input("\n\n\n Is this the right index location? : (y/Y) for yes (n/N) for no : ")
                           if resl == 'y' or resl == 'Y':
                              flag=True
                              return i
                           else:
                              print('\nJumping to next match .... \n\n')
                  if flag is True:
                     break
            elif response == 'n' or response == 'N':
                 return 0

      def book_read(self,data, pointer): #book pages printing function
          if pointer==0:
              print("\nStarting from beginning : \n")
          else:
              print("\n\nResuming from last keyword : \n")
          while True:
             print(data[pointer: pointer+2000])
             pointer+=200
         
             res2=input("(\n\ny/Y)next page (n/N) to stop. \n\n\n")
             if res2=='y' or res2=='Y':
                pass
             else:
                print('\n\n Saving last read index location ...')
                return pointer 
    
    
    
name=input("Enter your name: ")
obj1=Store(name)
data=obj1.book_selection()
pointer=obj1.keyword_search(data)
new_pointer=obj1.book_read(data,pointer)



