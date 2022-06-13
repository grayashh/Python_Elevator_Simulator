import random

class Building:
    number_of_floors = 0
    customer_list = []
    elevator = 0

    def __init__(self, floors, customers):                                                                                        
        self.number_of_floors = floors
        self.customer_num = customers
        for customerID in range(1, customers + 1):
            new = Customer(customerID, self.number_of_floors)
            self.customer_list.append(new)
        self.customer_list.sort(key = lambda x: x.customerID)
        self.elevator = Elevator(floors)
        self.run()

    def run(self):
        while (len(self.elevator.exit_list) < self.customer_num):
            self.output()
        print('All Customer Arrived at Destination')

    def output(self):
        #ELEVATOR MOVING UP LOOP
        while (self.elevator.current_floor < self.elevator.number_of_floors):
            self.elevator.current_floor +=1
            if not (self.elevator.current_floor == 1):
                print(f"Elevator : {(self.elevator.current_floor-1)} -> {self.elevator.current_floor}")
            if (self.elevator.current_floor == self.elevator.number_of_floors):
                print("The Elevator is on the Top Floor Now")
            for customer in self.customer_list:
                if (self.elevator.current_floor == customer.current_floor) & (customer.in_elevator == False) & (customer not in self.elevator.exit_list):
                    customer.in_elevator = True
                    self.elevator.register_customer(customer)
                    print(f"Customer {customer.customerID} -> Elevator")

                if (self.elevator.current_floor == customer.destination_floor) & (customer.in_elevator == True):
                    customer.finished = True
                    customer.in_elevator = False
                    self.elevator.cancel_customer(customer)
                    self.elevator.exit_customer(customer)
                    print(f"Customer {customer.customerID} -> Destination Floor")

            print(f"Elevator\'s Current Floor : {self.elevator.current_floor} \t Elevator\'s direction: up")   
            print("Customer:")
            for customer in self.customer_list:
                print(f"\tCustomer {customer.customerID} \tcurrent floor : {customer.current_floor} \tdestination floor : {customer.destination_floor}")
                print(f"\t\t\tin Elevator : {customer.in_elevator} \tis Finished : {customer.finished}")
            
            print('\n->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->\n')



        #ELEVATOR MOVING DOWN LOOP
        while (self.elevator.current_floor <= self.elevator.number_of_floors) & (self.elevator.current_floor > 1):
            self.elevator.current_floor -= 1
            print(f"Elevator : {(self.elevator.current_floor+1)} -> {self.elevator.current_floor}")

            for customer in self.customer_list:
                if (self.elevator.current_floor == customer.current_floor) & (customer.in_elevator == False) & (customer not in self.elevator.exit_list):
                    customer.in_elevator = True
                    self.elevator.register_customer(customer)
                    print(f"Customer {customer.customerID} -> Elevator")
                if (self.elevator.current_floor == customer.destination_floor) & (customer.in_elevator == True):
                    customer.finished = True
                    customer.in_elevator = False
                    self.elevator.cancel_customer(customer)
                    self.elevator.exit_customer(customer)
                    print(f"Customer {customer.customerID} -> Destination Floor")
            print("\n")

            print(f"Elevator\'s Current Floor : {self.elevator.current_floor} \t Elevator\'s direction: down")
            print("Customer:")
            for customer in self.customer_list:
                print(f"\tCustomer {customer.customerID} \tcurrent floor : {customer.current_floor} \tdestination floor : {customer.destination_floor}")
                print(f"\t\t\tin Elevator : {customer.in_elevator} \tis Finished : {customer.finished}")

            print('\n->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->\n')
        
class Elevator:
    number_of_floors = 0
    current_floor = 0
    up = 1
    down = -1

    def __init__(self, num_of_floors):
        self.number_of_floors = num_of_floors
        self.register_list = []
        self.exit_list = []
        self.current_floor = 0

    def move(self):
        pass;

    def register_customer(self, customer):
        self.register_list.append(customer)

    def cancel_customer(self, customer):
        self.register_list.remove(customer)

    def exit_customer(self, customer):
        self.exit_list.append(customer)


class Customer:
    current_floor = 0                                                                                                   
    destination_floor = 0                                                                                              
    customerID = 0                                                                                                      
    in_elevator = False                                                                                                
    finished = False 

    def __init__(self, customerID, floors):                                                                             
        self.customerID = customerID                                                                                   
        self.current_floor = random.randint(1, floors)                                                                
        self.destination_floor = random.randint(1, floors)
        while(self.destination_floor == self.current_floor):
            self.destination_floor = random.randint(1, floors)

def main():                                                                                                             
    floors = input('Input num_of_floors: ')
    while not (floors.isdigit()):
        print("Wrong Input!!!")
        floors = input('Input num_of_floors: ')
        
        
    customers = input('Input_num_of_customers: ')
    while not (customers.isdigit()):
        print("Wrong Input!!!")
        customers = input('Input_num_of_customers: ')
        
    print("\n")
    
    floors = int(floors)
    customers = int(customers)
    
    building = Building(floors, customers)
    
main()