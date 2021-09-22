class Menber:
    
    def __init__(self, no: int,name:str,weight:float)->None:
        self.no=no
        self.name=name
        self.weight=weight

    def print(self)->None:
        print("{}:{} {}kg".format(self.no,self.name,self.weight))

yamada=Menber(15,"山田太郎",72.7)
sekine=Menber(37,"関根信彦",65.3)    

yamada.print()
sekine.print()