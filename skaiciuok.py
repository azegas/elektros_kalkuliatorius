def calculate_cost():
    # Step 1: Get the power consumption in watts (W) from the user
    watts = float(input("Enter the power consumption of the device in watts (W): "))

    # Step 2: Convert watts to kilowatts (1 kW = 1000 W)
    kilowatts = watts / 1000

    # Step 3: Calculate the energy consumption in kilowatt-hours (kWh) assuming the device runs 24 hours a day
    kwh_per_day = kilowatts * 24

    # Step 4: Assume the cost of electricity is 0.13 euro cents per kWh
    cost_per_kwh = 0.22

    # Step 5: Calculate the cost for running the device for 24 hours daily, weekly, and monthly
    hourly_cost = kilowatts * cost_per_kwh
    daily_cost = hourly_cost * 24
    weekly_cost = daily_cost * 7
    monthly_cost = daily_cost * 30  # Assuming 30 days in a month
    yearly_cost = daily_cost * 365

    # Step 6: Print the results
    print(f"\nDevice power consumption: {kilowatts:.2f} kW")
    print(f"Hourly cost of running the device: €{hourly_cost:.2f}")
    print(f"Daily energy consumption: {kwh_per_day:.2f} kWh")
    print(f"Daily cost of running the device: €{daily_cost:.2f}")
    print(f"Weekly cost of running the device: €{weekly_cost:.2f}")
    print(f"Monthly cost of running the device: €{monthly_cost:.2f}")
    print(f"Yearly cost of running the device: €{yearly_cost:.2f}")


# Run the calculation
calculate_cost()
