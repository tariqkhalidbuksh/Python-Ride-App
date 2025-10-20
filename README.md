Smart Ride Booking App: OOP Analysis

This repository contains a simple Python console application designed to demonstrate the fundamental principles of Object-Oriented Programming (OOP), including Inheritance, Polymorphism, Encapsulation, and Composition.

The application simulates a basic ride-booking service where fares are calculated based on vehicle type and modified by user-specific discounts.

Core OOP Concepts Demonstrated

1. The Vehicle Hierarchy (Inheritance and Polymorphism)

This structure uses Inheritance where specialized vehicles (Car, Bike, Bus) inherit common logic from the base Vehicle class. Polymorphism (Method Overriding) is used to customize the fare calculation for each type.

Vehicle (The Base Class)

Method/Attribute

Concept

Explanation

__init__(self, brand, rate_per_km)

Constructor

Initializes the vehicle with a brand and its base rate_per_km.

calculate_fare(self, distance)

Base Logic

Defines the default fare formula. It applies a fixed surcharge: $100$ Rs for distances under $50$ km and $250$ Rs for $50$ km and over.

$$\text{Base Fare} = (\text{Distance} \times \text{Rate per km}) + \begin{cases} 100 & \text{if distance} < 50 \\ 250 & \text{if distance} \ge 50 \end{cases}$$

Derived Classes (Car, Bike, Bus)

Each child class overrides the base calculate_fare method:

Class

Concept

Specific Logic (Overridden calculate_fare)

Car(Vehicle)

Method Overriding

Adds a fixed $50$ Rs service charge on top of the base fare.

Bike(Vehicle)

Method Overriding

Applies a $10\%$ discount to the base fare.

Bus(Vehicle)

Method Overriding

Applies a $200$ Rs discount only if the distance is greater than $100$ km.

2. The Booking System (Encapsulation and Composition)

User Class

Handles user identity and discount eligibility.

Method/Attribute

Concept

Explanation

get_discount(self)

Conditional Logic

Returns a $20\%$ ($0.2$) discount rate if the user is under $18$ OR is a student. Otherwise, returns $0.0$.

RideBooking Class

This class manages the booking process, showcasing Composition (it has a User object) and Encapsulation.

Method/Attribute

Concept

Explanation

__init__(self, user)

Composition

Holds a reference to the User object to apply discounts.

__apply_discount(self, fare)

Encapsulation

A private method (indicated by __) that handles the secure, internal logic of applying the user's discount.

add_ride(self, vehicle, distance)

Core Logic

Orchestrates the entire calculation: calls the vehicle's fare logic and then applies the user's final discount.

show_summary(self)

Reporting

Displays all booked rides and the total final payable amount.

Key Takeaways

OOP Principle

Relationship

Example from Code

Inheritance

Is-A

A Car is a Vehicle.

Polymorphism

Customization

All vehicles have calculate_fare, but they run different code.

Composition

Has-A

RideBooking has a User object.

Encapsulation

Hiding Details

The private __apply_discount method handles complex logic internally.

How to Run the Application

To run the application, ensure you have Python installed.

Save the original code as a file named ride_booking_app.py.

Open your terminal or command prompt.

Run the script:

python ride_booking_app.py


Follow the interactive prompts to enter user details and book rides. The summary will update after each booking.
