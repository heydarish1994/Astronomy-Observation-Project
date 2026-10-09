from database import (
    create_table,
    add_observation,
    get_all_observations,
    search_observation,
    delete_observation,
    update_observation,
    save_to_csv,
)

from visual import (
    show_data,
    show_first_observations,
    show_last_observations,
    show_columns,
    show_data_info,
    search_by_target,
    search_by_observer,
    filter_by_exposure,
    search_by_observer_and_exposure,
    sort_by_exposure,
    show_exposure_sum,
    show_exposure_mean,
    equations_observations,
    plot_observations,
    plot_observer_exposure,
    plot_target_exposure,
)


def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")


def read_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter an integer.")


def add_new_observation():
    target = input("Enter target: ")
    observer = input("Enter observer: ")
    filter_name = input("Enter filter name: ")

    exposure = read_number("Enter exposure: ")

    wavelength = read_number("Enter wavelength: ")

    magnitude = read_number("Enter magnitude: ")

    add_observation(target, observer, filter_name, exposure, wavelength, magnitude)

    print("Observation added successfully.")


def show_observation_list():
    observations = get_all_observations()

    if not observations:
        print("No observations found.")
        return

    for observation in observations:
        print("\n--------------------")
        observation.display_info()


def search_observations():
    print("\nSearch options:")
    print("1. Search by target")
    print("2. Search by observer")
    print("3. Search by target and observer")

    choice = input("Enter your choice: ")

    if choice == "1":
        target = input("Enter target: ")

        results = search_observation(target=target)

    elif choice == "2":
        observer = input("Enter observer: ")

        results = search_observation(observer=observer)

    elif choice == "3":
        target = input("Enter target: ")

        observer = input("Enter observer: ")

        results = search_observation(target=target, observer=observer)

    else:
        print("Invalid choice.")
        return

    if not results:
        print("No observations found.")
        return

    for observation in results:
        print("\n--------------------")
        observation.display_info()


def delete_existing_observation():
    observation_id = read_integer("Enter observation ID: ")

    deleted = delete_observation(observation_id)

    if deleted:
        print("Observation deleted successfully.")
    else:
        print("Observation not found.")


def update_existing_observation():
    observation_id = read_integer("Enter observation ID: ")

    target = input("Enter new target: ")

    observer = input("Enter new observer: ")

    filter_name = input("Enter new filter name: ")

    exposure = read_number("Enter new exposure: ")

    wavelength = read_number("Enter new wavelength: ")

    magnitude = read_number("Enter new magnitude: ")

    updated = update_observation(
        observation_id, target, observer, filter_name, exposure, wavelength, magnitude
    )

    if updated:
        print("Observation updated successfully.")
    else:
        print("Observation not found.")


def data_analysis():
    print("\n===== Data Analysis =====")

    print("\n--- All Data ---")
    show_data()

    print("\n--- First Observations ---")
    show_first_observations()

    print("\n--- Last Observations ---")
    show_last_observations()

    print("\n--- Columns ---")
    show_columns()

    print("\n--- Data Info ---")
    show_data_info()

    print("\n--- Sorted by Exposure ---")
    sort_by_exposure()

    print("\n--- Exposure Sum ---")
    show_exposure_sum()

    print("\n--- Exposure Mean ---")
    show_exposure_mean()

    print("\n--- Sum and Mean by Observer ---")
    equations_observations()


def search_with_pandas():
    print("\n===== Pandas Search =====")

    print("1. Search by target")
    print("2. Search by observer")
    print("3. Filter by exposure")
    print("4. Observer and exposure")

    choice = input("Enter your choice: ")

    if choice == "1":
        target = input("Enter target: ")

        search_by_target(target)

    elif choice == "2":
        observer = input("Enter observer: ")

        search_by_observer(observer)

    elif choice == "3":
        min_exposure = read_number("Enter minimum exposure: ")

        filter_by_exposure(min_exposure)

    elif choice == "4":
        observer = input("Enter observer: ")

        min_exposure = read_number("Enter minimum exposure: ")

        search_by_observer_and_exposure(observer, min_exposure)

    else:
        print("Invalid choice.")


def charts():
    print("\n===== Charts =====")

    print("1. Observation exposure")
    print("2. Observer exposure")
    print("3. Target exposure")

    choice = input("Enter your choice: ")

    if choice == "1":
        plot_observations()

    elif choice == "2":
        plot_observer_exposure()

    elif choice == "3":
        plot_target_exposure()

    else:
        print("Invalid choice.")


def main():
    create_table()

    while True:
        print("\n")
        print("=" * 45)
        print("ASTRONOMY OBSERVATION PROJECT")
        print("=" * 45)

        print("1. Add observation")
        print("2. Show observations")
        print("3. Search observation")
        print("4. Delete observation")
        print("5. Update observation")
        print("6. Export to CSV")
        print("7. Data analysis")
        print("8. Pandas search and filter")
        print("9. Charts")
        print("10. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                add_new_observation()

            elif choice == "2":
                show_observation_list()

            elif choice == "3":
                search_observations()

            elif choice == "4":
                delete_existing_observation()

            elif choice == "5":
                update_existing_observation()

            elif choice == "6":
                save_to_csv()

            elif choice == "7":
                data_analysis()

            elif choice == "8":
                search_with_pandas()

            elif choice == "9":
                charts()

            elif choice == "10":
                print("Goodbye.")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Please enter a valid value.")


if __name__ == "__main__":
    main()
