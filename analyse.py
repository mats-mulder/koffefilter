import json
import math

if __name__ == '__main__':

    departements = ["62", "59", "80", "60", "02", "08", "51", "10", "52", "55", "54", "88", "57", "67", "68", "70"]

    totals = {}

    # Loop through the department numbers
    for department in departements:
        # Open the file for the current department
        with open(f"{department}.json", "r") as file:
            # Loop through the lines in the file
            for line in file:
                # Parse the JSON data from the line
                data = json.loads(line)
                # Get the value of "valeur_fonciere" for the current row
                value = data["valeur_fonciere"]
                # Convert the value to a float
                try:
                    value = float(value)
                except ValueError:
                    # If the value is not a valid number, skip it
                    continue
                # Check if the value is not nan
                if not math.isnan(value):
                    # Add the value to the total for the department
                    if department in totals:
                        # Increment the item count for the department
                        totals[department]["count"] += 1
                        # Add the value to the total for the department
                        totals[department]["total"] += value
                    else:
                        # Initialize the item count and total for the department
                        totals[department] = {
                            "count": 1,
                            "total": value
                        }

    # Dictionary to store the average value of "valeur_fonciere" for each department
    averages = {}

    # Loop through the departments
    for department, total in totals.items():
        # Calculate the average value for the department
        average = total['total'] / total['count']
        # Add the average to the dictionary
        averages[department] = average

    # Print the average values for each department
    for department, average in averages.items():
        print(f"Department {department}: {average}")