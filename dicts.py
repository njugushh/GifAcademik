# keys have to be unique

month_conversions = {
     0: "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "Ma": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(month_conversions[0])    # Gives us the value of the key
print(month_conversions.get("Sep"))
print(month_conversions.get("Luv", "Not a valid key"))  # gives a default value
