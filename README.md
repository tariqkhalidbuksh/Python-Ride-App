# Smart Ride Booking App > ( OOP Principles in Python )

This repository contains a simple **Python console application** designed to demonstrate the **fundamental principles of Object-Oriented Programming (OOP)**.  
It provides a clear and concise example of how to implement:

- **Inheritance**  
- **Polymorphism**  
- **Encapsulation**  
- **Composition**

The application simulates a basic **ride-booking service** where fares are calculated based on vehicle type and adjusted by user-specific discounts.

---

## Core OOP Concepts Demonstrated

### 1. Vehicle Hierarchy (Inheritance and Polymorphism)

The structure uses **Inheritance**, where specialized vehicles (`Car`, `Bike`, `Bus`) inherit common logic from the base `Vehicle` class.  
**Polymorphism (Method Overriding)** is used to customize fare calculation for each type.

#### Vehicle (Base Class)

| Method/Attribute | Concept | Explanation |
|------------------|----------|--------------|
| `__init__(self, brand, rate_per_km)` | Constructor | Initializes the vehicle with a brand and its base rate per km. |
| `calculate_fare(self, distance)` | Base Logic | Calculates fare with a conditional surcharge. |

> **Important:** The surcharge is applied **conditionally**:  
> - Rs. 100 if distance < 50 km  
> - Rs. 250 if distance ≥ 50 km  

**Correct Base Fare Formula:**

```python
Base Fare = (distance * rate_per_km) + (100 if distance < 50 else 250)
````

---

### Derived Classes (Overridden Fare Logic)

| Class           | Concept           | Specific Logic                                                           |
| --------------- | ----------------- | ------------------------------------------------------------------------ |
| `Car(Vehicle)`  | Method Overriding | Adds a fixed Rs.50 to the base fare.                                       |
| `Bike(Vehicle)` | Method Overriding | Applies a **10% discount** to the base fare.                             |
| `Bus(Vehicle)`  | Method Overriding | Applies a **Rs.200 discount** only if the distance is greater than 100 km. |

---

### Example Code

```python
class Vehicle:
    def __init__(self, brand, rate_per_km):
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
        return base_fare + 50


class Bike(Vehicle):
    def calculate_fare(self, distance):
        base_fare = super().calculate_fare(distance)
        return base_fare * 0.9  # 10% discount


class Bus(Vehicle):
    def calculate_fare(self, distance):
        base_fare = super().calculate_fare(distance)
        if distance > 100:
            base_fare -= 200
        return base_fare
```

---

## 2. Booking System (Encapsulation and Composition)

### User Class

Handles user identity and discount eligibility.

| Method/Attribute     | Concept           | Explanation                                                                                             |
| -------------------- | ----------------- | ------------------------------------------------------------------------------------------------------- |
| `get_discount(self)` | Conditional Logic | Returns **20% (0.2)** discount if the user is under 18 **or** is a student. Otherwise, returns **0.0**. |

#### Example:

```python
class User:
    def __init__(self, name, age, is_student=False):
        self.name = name
        self.age = age
        self.is_student = is_student

    def get_discount(self):
        if self.age < 18 or self.is_student:
            return 0.2
        return 0.0
```

---

### RideBooking Class

Manages the booking process, showcasing **Composition** and **Encapsulation**.

| Method/Attribute                    | Concept       | Explanation                                                                       |
| ----------------------------------- | ------------- | --------------------------------------------------------------------------------- |
| `__init__(self, user)`              | Composition   | Holds a reference to the `User` object to apply discounts.                        |
| `__apply_discount(self, fare)`      | Encapsulation | Private method that applies the user’s discount internally.                       |
| `add_ride(self, vehicle, distance)` | Core Logic    | Coordinates the booking flow—calls vehicle fare logic and applies user discounts. |
| `show_summary(self)`                | Reporting     | Displays all booked rides and the total payable amount.                           |

#### Example:

```python
class RideBooking:
    def __init__(self, user):
        self.user = user
        self.rides = []

    def __apply_discount(self, fare):
        discount_rate = self.user.get_discount()
        return fare - (fare * discount_rate)

    def add_ride(self, vehicle, distance):
        fare = vehicle.calculate_fare(distance)
        final_fare = self.__apply_discount(fare)
        self.rides.append((vehicle.brand, distance, final_fare))

    def show_summary(self):
        print("\n--- Ride Summary ---")
        total = 0
        for brand, distance, fare in self.rides:
            print(f"Vehicle: {brand} | Distance: {distance} km | Fare: Rs {fare:.2f}")
            total += fare
        print(f"\nTotal Payable: Rs {total:.2f}")
```

---

## Key Takeaways

| OOP Principle     | Relationship   | Example                                                           |
| ----------------- | -------------- | ----------------------------------------------------------------- |
| **Inheritance**   | Is-A           | A Car is a Vehicle.                                               |
| **Polymorphism**  | Customization  | All vehicles have `calculate_fare`, but they run different logic. |
| **Composition**   | Has-A          | `RideBooking` has a `User` object.                                |
| **Encapsulation** | Hiding Details | The private `__apply_discount()` handles logic internally.        |

---

## Getting Started

### Prerequisites

* Python 3.x installed on your system.

### Run Instructions

1. Save the code as **`ride_booking_app.py`**
2. Open a terminal or command prompt.
3. Navigate to the file’s directory.
4. Run:

   ```bash
   python ride_booking_app.py
   ```
5. Follow the interactive prompts to:

   * Enter user details
   * Select vehicle type
   * Enter ride distance

A summary of your rides and total fare will be displayed at the end.

---

## Example OOP Relationships

```
User ─────▶ RideBooking ─────▶ Vehicle
                   │
        ├── Car (inherits Vehicle)
        ├── Bike (inherits Vehicle)
        └── Bus  (inherits Vehicle)
```



## Educational Purpose

This project is ideal for beginners who want to **see OOP concepts in action** using a real-world example of ride booking and fare calculation.



### Author

**Tariq Khalid Buksh**
*Python Instructor & Developer*




