class Resturant():
    def __init__(self):
        self.menu={"Idli": 30,
                    "Dosa": 50,
                    "Masala Dosa": 70,
                    "Vada": 25,
                    "Poori": 40,
                    "Upma": 35,
                    "Veg Biryani": 120,
                    "Paneer Butter Masala": 150,
                    "Fried Rice": 100,
                    "Tea": 15,
                    "Coffee": 20}
        self.order={}
    def Show_menu(self):
        if not self.menu.items():
            print("no food available in the Resturant Mennu")
        else:
            
            for k,v in self.menu.items():
                print(f"{k}--->{v}")
    def add_item(self):
        while True:
            
            item_name=input("Enter the name")
            if item_name.lower()=='none':
                break
            if item_name in self.menu:
                qty=input("Enter the qty")
                if item_name in self.order:
                    self.order[item_name]+=qty
                else:
                    self.order[item_name]=qty
                print(f'{item_name} is {qty} be added Successfully')
            else:
                print(f'{item_name} is not available in the menu')
    def show_additem(self):
        if not self.order:
            print("not food you can order")
        else:
            for i,v in self.order.items():
                print(f"{i}--->{v}")
    def update_item(self,item_name,qty):
        if item_name in self.order:
            self.order[item_name]=qty
            print(f"{item_name} is {qty} can be update successfully")
        else:
            print(f'{item_name} is not in order to update' )
    def remove_item(self,item_name):
        if item_name in self.order:
            del self.order[item_name]
            print(f'{item_name} is deleted successfully')
        else:
            print(f'{item_name} not found')
    def search(self,item_name):
        if item_name in self.order:
            print(f'{item_name }-->{self.order[item_name]}')
        else:
            print(f'{item_name} not found')
    def Total(self):
        t=0
       
        print("Resturant")
        print("-"*20)
        
        for item_name,qty in self.order.items():
            qty=int(qty)
            p=self.menu[item_name]*qty
            print(f"{item_name}-->{qty}={p}")
            t=t+p
            
        print("-"*20)
        print("Total",t)
        print("-"*20)
e=Resturant()
while True:
    print("1.show menu")
    print("2. add_item")
    print("3.show addItem")
    print("4.update_Item")
    print("5. remove_item")
    print("6. search_item")
    print("7. Total")
    print("8.Exit")
    ch=int(input())
    if ch==1:
        e.Show_menu()
    elif ch==2:
        e.add_item()
    elif ch==3:
        e.show_additem()
    elif ch==4:
        item_name=input("Enter the Item name")
        qty=int(input("Enter the qty"))
        e.update_item(item_name,qty)
    elif ch==5:
        item_name=input("Enter the Item name")
        e.remove_item(item_name)
    elif ch==6:
        item_name=input("Enter the Item name")
        e.search(item_name)
    elif ch==7:
        e.Total()
    elif ch==8:
        break
        
        
        
        
        
        
        
       


            
           
            