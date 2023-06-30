import csv
import matplotlib.pyplot as plt

def get_popular_name(year, gender):
    filename = "baby_names_large.csv"
    popular_name = None
    max_percent = 0

    with open(filename, "r") as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            if int(row["year"]) == year and row["sex"] == gender:
                percent = float(row["percent"])

                if percent > max_percent:
                    max_percent = percent
                    popular_name = row["name"]

    return popular_name

def get_popular_years(name, gender):
    filename = "baby_names_large.csv"
    popular_years = []

    with open(filename, "r") as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            if row["name"] == name and row["sex"] == gender:
                year = int(row["year"])
                percent = float(row["percent"])

                if percent > 0:
                    popular_years.append((year, percent))

    return popular_years

# Main program
while True:
    print("Menu:")
    print("1. Find the most popular name")
    print("2. Find the year(s) when a name was most popular")
    print("3. Generate a list of name popularity by year")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        year = int(input("Enter the year: "))
        gender = input("Enter the gender (boy/girl): ")

        popular_name = get_popular_name(year, gender)

        if popular_name:
            print(f"The most popular {gender} name in {year} was: {popular_name}")
        else:
            print("No data found for the specified year and gender.")
    elif choice == "2":
        name = input("Enter the name: ")
        gender = input("Enter the gender (boy/girl): ")

        popular_years = get_popular_years(name, gender)

        if popular_years:
            if len(popular_years) == 1:
                print(f"{name} was most popular in the year: {popular_years[0][0]}")
            else:
                years = ', '.join(str(year[0]) for year in popular_years)
                print(f"{name} was most popular in the years: {years}")
        else:
            print("No data found for the specified name and gender.")
    elif choice == "3":
        name = input("Enter the name: ")
        gender = input("Enter the gender (boy/girl): ")

        name_popularity = get_popular_years(name, gender)

        if name_popularity:
            print(f"List of {name}'s popularity by year:")
            for year, popularity in name_popularity:
                print(f"Year: {year}, Popularity: {popularity}")

            years = [year for year, _ in name_popularity]
            popularities = [popularity for _, popularity in name_popularity]

            plt.plot(years, popularities)
            plt.xlabel("Year")
            plt.ylabel("Popularity")
            plt.title(f"Popularity of {name} ({gender.capitalize()}) Over Time")
            plt.savefig("name_popularity.pdf", format="pdf")
            plt.show()
            break
        else:
            print("No data found for the specified name and gender.")
   
