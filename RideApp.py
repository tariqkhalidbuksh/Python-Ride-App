
class Vehicle:
    def __init__(self, brand , rate_per_km):
        self.brand = brand
        self.rate_per_km = rate_per_km

    
    def calculate_fare(self, distance):
        if distance < 50:
            return distance * self.rate_per_km + 100
        else:
            return distance * self.rate_per_km + 250
        
    
class Car(Vehicle):
    def calculate_fare(self, distance):
        base_fare = super().calculate_fare(distance)
        service_charge = 50
        return base_fare + service_charge
    

class Bike(Vehicle):
    def calculate_fare(self, distance):
        base_fare = super().calculate_fare(distance)
        discount = 0.1 #10%
        return base_fare - (base_fare * discount)
    

class Bus(Vehicle):
    def calculate_fare(self, distance):
        base_fare = super().calculate_fare(distance)
        if distance > 100:
            base_fare -= 200 #discount 
        return base_fare
    
#BLUEPRINT READY ------------------------------------------->>>

class User:
    def __init__(self,name, age, is_student=False):
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def get_discount(self):
        if self.age < 18 or self.is_student:
            return 0.2 # 20% discount more
        return 0.0
    

class RideBooking:
    def __init__(self,user):
        self.user = user
        self.__ride = []
    
    def __apply_discount(self, fare):
        discount = self.user.get_discount()
        return fare - (fare * discount)
    
    def add_ride(self , vehicle , distance):
        fare = vehicle.calculate_fare(distance)
        final_fare = self.__apply_discount(fare)
        self.__ride.append((vehicle.brand , distance , fare , final_fare))


        print(f"Ride Booked with {vehicle.brand} for {distance} km.")
        print(f"Base Fare : Rs. {fare:.2f}")
        if self.user.get_discount() > 0:
            print("Discount Applied (20%)")
        print(f"Final Fare : Rs. {final_fare:.2f}")
    
    def show_summary(self):
        print("========================Ride Summray========================")
        total = 0
        for brand, dist, fare, final in self.__ride:
            print(f"{brand:10} | {dist} KM | Base : Rs.{fare:.2f} | Final : Rs. {final:.2f}")
            total += final
        print("-------------------------------------------------------------")
        print(f"Total Payable Amount : Rs. {total:.2f}")




def main():
     print("======================== Welcome to Smart Ride Booking App ========================")


     name = input("Enter Your Full Name Here : ")
     age = int(input("Enter Your Age Here : "))
     is_student_input = input("Are you a student ? (yes / no) : ").lower()
     is_student = True if is_student_input == "yes" else False


     user = User(name ,age , is_student)
     booking = RideBooking(user)


     while True:
         print("Select Your Vehicle Type : ")
         print("1. Car")
         print("2. Bike")
         print("3. Bus")
         print("4. Exit")

         choice = input("Enter your Choice here : ").lower()
         if choice in ['4','exit']:
             break
         
         distance = float(input("Enter Your Distance ( in KM ) "))
         if choice == "1" or choice == "car":
             Vehicle = Car("Honda Civic" , 50)
         elif choice == "2" or choice == "bike":
             Vehicle = Bike("Honda 125" , 25)
         elif choice == "3" or choice == "bus":
             Vehicle = Bus("Daewoo" , 10)
         else:
             print("Invaild Option . Try again !")
             continue
         
         booking.add_ride(Vehicle, distance)
         
         booking.show_summary()
         print("Thank you for using smart Riding App")






#Run Program 

if __name__ == "__main__":
    main()

        
             



