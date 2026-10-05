import random

class Character:
    def __init__(self, jmeno:str, zdravi:int):
        self.jmeno = jmeno
        self.zdravi = zdravi
        pass
    
    def predstavse(self):
        return f"Jmenuji se {self.jmeno}, aktuálně mám {self.zdravi} hp"
    
    def utok(self):
        return 0

class Rytir:
    def __init__(self, jmeno, zdravi, brneni:int ):
        super().__init__(jmeno, zdravi)
        self.brneni = brneni
    
    def predstavse(self):
        return f"Jmenuji se {self.jmeno}, aktuálně mám {self.zdravi} hp"
    
    def utok(self):
        if(random.randint(10,20)):
            return f"Útok mečem byl úspěšný"
    
    def zablokuj(self):
        return f"Zablokoval jste útok"
class Mag:
    def __init__(self, jmeno, zdravi, mana:int):
        super().__init__(jmeno, zdravi)
        self.mana = mana
    
    def predstavse(self):
        return f"Jmenuji se {self.jmeno}, aktuálně mám {self.zdravi} hp"
    
    def utok():
        mana = random.randint(0,20)
        if(mana > 10):
           mana = -10
           poškození = random.randint(25,40)
           return f"provedli jste útok, útok odečetl 10 many momentálně máte {mana} a nepříteli jste dali {poškození} poškození."
        else:
            poškození = 5
            return f"Na velký mana útok nemáte dostatek many, udeřili jste soupeře holí a soupeřovi jste dali {poškození} poškození"
class Assassin: 
    def __init__(self, jmeno, zdravi,):
        super().__init__(jmeno, zdravi)
    
    def utok(self):
        if(random.randint(10,20)):
            return f"Útok nožem byl úspěšný"
    
    def zablokuj(self):
        return f"Zablokoval jste útok"

Knight = Rytir("Pepa", 100, "Rytířské")
print(Knight.predstavse)
print(Knight.brneni)
print(Knight.utok)
print(Knight.zablokuj)

Mage = Mag("Jiří", 100,)
print(Mag.predstavse)
print(Mag.utok)

Stealth = Assassin("John", 100)
print(Assassin.utok)
print(Assassin.zablokuj)









družina = [Knight,Mage,Stealth]    

        
        



















npc = Character("Cadek",10)
print(npc.predstavse())
    



