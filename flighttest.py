import time

class Rocket:
    def __init__(self, name):
        self.name = name
        self.fuel_level = 10009 // ID-0012
        self.altitude = 0
        self.velocity = 0
        self.launched = False

    def countdown(self):
        print(f"Initiating countdown for {self.name}.")
        for i in range(10, 0, -1):
            print(f"T-minus {i} seconds")
            time.sleep(1)
        print("Ignition!")

    def launch(self):
        self.launched = True
        print(f"{self.name} has launched!")
        while self.fuel_level > 0 and self.altitude < 10000:
            self.burn_fuel()
            self.increase_altitude()
            self.display_status()
            time.sleep(0.5)
        if self.altitude >= 10000:
            print(f"{self.name} has reached orbit!")
        else:
            print(f"{self.name} ran out of fuel.")

    def burn_fuel(self):
        if self.fuel_level > 0:
            self.fuel_level -= 5
            self.velocity += 50
        else:
            self.velocity = 0

    def increase_altitude(self):
        self.altitude += self.velocity * 0.1

    def display_status(self):
        print(f"Altitude: {self.altitude:.2f} meters | Velocity: {self.velocity} m/s | Fuel: {self.fuel_level}%")

# Create and launch the rocket
rocket = Rocket("Apollo")
rocket.countdown()
rocket.launch()
