from car_park_stack import Stack, Car

def main():
    Car_Lane = Stack()

    while True:
        print("\n--- MENU ---")
        print("(1) Arrive")
        print("(2) Depart")
        print("(3) Exit")
        choice = input("Select: ")

        if choice == '1':
            print("\n[A] Manual Entry")
            print("[B] Random Generate")
            sub_choice = input("Select: ").upper()

            if sub_choice == 'A':
                plate = input("Enter Plate Number: ").upper()
                new_car = Car(plate)
                Car_Lane.push(new_car)
                print(f"Car {new_car.plate_number} entered the lane at Slot {Car_Lane.size()}.")

            elif sub_choice == 'B':
                new_car = Car()
                Car_Lane.push(new_car)
                print(f"Car {new_car.plate_number} entered the lane at Slot {Car_Lane.size()}.")

        elif choice == '2':
            if Car_Lane.isEmpty():
                print("\nLane is empty.")
            else:
                target = input("\nEnter plate number to be removed: ").upper()
                success = Car().remove_car(Car_Lane, target)

                if success:
                    print(f"\nCar {target} has successfully departed.")
                else:
                    print(f"\nCar {target} not found in the lane.")

        elif choice == '3':
            print("Exiting system...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()