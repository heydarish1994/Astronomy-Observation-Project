class Observation:
    def __init__(
        self,
        target,
        observer,
        filter_name,
        exposure,
        wavelength,
        magnitude,
        observation_id=None
    ):
        self.observation_id = observation_id
        self.target = target
        self.observer = observer
        self.filter_name = filter_name
        self.exposure = exposure
        self.wavelength = wavelength
        self.magnitude = magnitude

    def display_info(self):
        print(f"ID: {self.observation_id}")
        print(f"Target: {self.target}")
        print(f"Observer: {self.observer}")
        print(f"Filter Name: {self.filter_name}")
        print(f"Exposure: {self.exposure} seconds")
        print(f"Wavelength: {self.wavelength} Angstroms")
        print(f"Magnitude: {self.magnitude}")


def observation_from_row(row):
    return Observation(
        target=row[1],
        observer=row[2],
        filter_name=row[3],
        exposure=row[4],
        wavelength=row[5],
        magnitude=row[6],
        observation_id=row[0]
    )