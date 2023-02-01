from Wild_Cat_Zoo.Lion import Lion
from Wild_Cat_Zoo.Tiger import Tiger
from Wild_Cat_Zoo.Caretaker import Caretaker
from Wild_Cat_Zoo.Cheetah import Cheetah
from Wild_Cat_Zoo.Keeper import Keeper
from Wild_Cat_Zoo.Vet import Vet

class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"
        elif self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        the_workers = [worker for worker in self.workers if worker.name == worker_name]
        if the_workers:
            current_worker = the_workers[0]
            self.workers.remove(current_worker)
            return f"{worker_name} fired successfully"
        else:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries_cost = 0
        for worker in self.workers:
            salaries_cost += worker.salary
        if self.__budget < salaries_cost:
            return f"You have no budget to pay your workers. They are unhappy"
        self.__budget -= salaries_cost
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        tend_cost = 0
        for animal in self.animals:
            tend_cost += animal.get_needs()
        if self.__budget < tend_cost:
            return f"You have no budget to tend the animals. They are unhappy."
        self.__budget -= tend_cost
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]
        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            result += repr(lion) + "\n"
        result += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            result += repr(tiger) + "\n"
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        for c in cheetahs:
            result += repr(c) + "\n"
        result = result[:-1]
        return result

    def workers_status(self):
        caretakers = [a for a in self.workers if a.__class__.__name__ == "Caretaker"]
        keepers = [a for a in self.workers if a.__class__.__name__ == "Keeper"]
        vets = [a for a in self.workers if a.__class__.__name__ == "Vet"]
        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        for keep in keepers:
            result += repr(keep) + "\n"
        result += f"----- {len(caretakers)} Caretakers:\n"
        for carer in caretakers:
            result += repr(carer) + "\n"
        result += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            result += repr(vet) + "\n"
        result =  result[:-1]
        return  result

zoo = Zoo("Zootopia", 3000, 5, 8)
# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
# Animal prices
prices = [200, 190, 204, 156, 211, 140]
# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))
    # Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))
    print(zoo.tend_animals())
    print(zoo.pay_workers())
    print(zoo.fire_worker("Adam"))
    print(zoo.animals_status())
    print(zoo.workers_status())