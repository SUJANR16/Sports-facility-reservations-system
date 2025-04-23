import datetime

# Facilities and their reservations: { 'facility_name': [reservation_times] }
facilities = {
    'Tennis Court': [],
    'Basketball Court': [],
    'Swimming Pool': []
}

def view_facilities():
    print("\n--- Available Sports Facilities ---")
    for facility in facilities:
        print(facility)

def view_reservations():
    print("\n--- Current Reservations ---")
    for facility, reservations in facilities.items():
        print(f"{facility}:")
        if not reservations:
            print("  No reservations.")
        else:
            for res in reservations:
                print(f"  {res['name']} reserved from {res['start_time']} to {res['end_time']}")

def reserve_facility():
    print("\n--- Reserve a Facility ---")
    name = input("Enter your name: ")
    view_facilities()
    facility = input("Enter the facility you want to reserve: ")

    if facility not in facilities:
        print(f"'{facility}' is not a valid facility.")
        return

    start_time_str = input("Enter start time (YYYY-MM-DD HH:MM): ")
    end_time_str = input("Enter end time (YYYY-MM-DD HH:MM): ")

    try:
        start_time = datetime.datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
        end_time = datetime.datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")

        if end_time <= start_time:
            print("End time must be later than start time.")
            return

        # Check if facility is available at the requested time
        for res in facilities[facility]:
            if (start_time < res['end_time'] and end_time > res['start_time']):
                print(f"Sorry, '{facility}' is already reserved during this time slot.")
                return

        # Add reservation
        facilities[facility].append({
            'name': name,
            'start_time': start_time,
            'end_time': end_time
        })
        print(f"Successfully reserved {facility} from {start_time} to {end_time}.")

    except ValueError:
        print("Invalid time format. Please use 'YYYY-MM-DD HH:MM'.")

def cancel_reservation():
    print("\n--- Cancel a Reservation ---")
    name = input("Enter your name: ")
    view_reservations()

    facility = input("Enter the facility you want to cancel the reservation for: ")

    if facility not in facilities:
        print(f"'{facility}' is not a valid facility.")
        return

    for res in facilities[facility]:
        if res['name'] == name:
            print(f"Found your reservation: {facility} from {res['start_time']} to {res['end_time']}")
            confirm = input("Are you sure you want to cancel this reservation? (yes/no): ").strip().lower()
            if confirm == 'yes':
                facilities[facility].remove(res)
                print("Your reservation has been canceled.")
            else:
                print("Reservation cancellation aborted.")
            return

    print(f"No reservation found under the name {name} for {facility}.")

def main():
    while True:
        print("\n=== Sports Facility Reservation System ===")
        print("1. View Facilities")
        print("2. View Reservations")
        print("3. Reserve a Facility")
        print("4. Cancel a Reservation")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == '1':
            view_facilities()
        elif choice == '2':
            view_reservations()
        elif choice == '3':
            reserve_facility()
        elif choice == '4':
            cancel_reservation()
        elif choice == '5':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option. Please select 1-5.")

if __name__ == "__main__":
    main()
