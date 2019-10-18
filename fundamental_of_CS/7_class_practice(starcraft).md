class Human:
    
    population = 0
    
    def __init__(self, max_health = 50):
        self.max_health = max_health
        self.health = max_health
        Human.population += 1
        self.status = "alive"
        
    def set_health(self, var, attack_kind):
        self.health += var
        if self.health > self.max_health:
            self.health = self.max_health
        elif self.health <= 0:
            self.health = 0
            self.status = "dead"
            
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):
        if status in ("alive", "dead"):
            self.__status = status
        if status == "dead":
            Human.population -= 1
            
    def summary(self):
        print("Health: {} : {}, Status : {}".format(self.health, self.max_health, self.status))


# Attacker class

from abc import *

class Attacker(Human, metaclass =ABCMeta):
    def __init__(self, attack_pow, attack_kind):
        super().__init__()
        self.attack_kind = attack_kind
        self.attack_pow = attack_pow
        self.kill_count = 0
        
    @abstractmethod
    def attack(self, other):
        pass
    
    


#class Marin

class Marin(Attacker):
    def __init__(self, attack_pow = 10, attack_kind = "rifle"):
        super().__init__(attack_pow, attack_kind)

    def attack(self, obj):
        if obj.status == "dead":
            print("already dead")
            return
        
        obj.set_health(-self.attack_pow, self.attack_kind)
        if obj.status == "dead":
            self.kill_count += 1
            print("kill")
        
    
    
        

#class Ghost

class Ghost(Attacker):
    def __init__(self, attack_pow = 7, attack_kind = "sniper rifle"):
        super().__init__(attack_pow, attack_kind)

    def attack(self, obj):
        if obj.status == "dead":
            print("already dead")
            return
        
        obj.set_health(-self.attack_pow, self.attack_kind)
        if obj.status == "dead":
            self.kill_count += 1
            print("kill")
        
    
    
        
class Medic(Human):
    def __init__(self, max_health = 60):
        super().__init__()
        self.heal_box = 3
        self.heal_pow = 30
        
    def set_health(self, var, attack_kind):
        if attack_kind == "sniper rifle":
            var *= 2
        self.health += var

    def heal(self, obj):
        if obj.status == "dead":
            print("already dead")
            return
        if self.heal_box <= 0:
            print("Don't have heal box")
            return
        
        if obj.status == "alive" and (obj.health < obj.max_health):
            obj.set_health(self.heal_pow, "heal")
            self.heal_box -= 1
        
    def summary(self):
        print("Health: {} : {}, Status : {}, healbox: {}".format(self.health, self.max_health, self.status, self.heal_box))



