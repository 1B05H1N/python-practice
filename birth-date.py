import datetime
import pytz

def get_birth_day(birthdate_str, birth_tz):
    # Parse the birthday string
    birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d %H:%M")
    birthdate = birth_tz.localize(birthdate)

    # Calculate the day of the week
    day_of_week = birthdate.strftime('%A')  # %A gives the full weekday name

    return day_of_week

def list_timezones_by_country(country_code):
    try:
        timezones = pytz.country_timezones[country_code]
    except KeyError:
        print(f"No timezones found for {country_code}. Please enter a valid country code.")
        return None
    return timezones

def main():
    # User input for country
    print("Please enter thetwo-letter country code where you were born (e.g., US for United States, GB for Great Britain):")
    country_code = input("Country Code: ").upper()

    # Get timezones for the country
    timezones = list_timezones_by_country(country_code)
    if not timezones:
        return  # Exit if no timezones are found or invalid country code is provided

    # List the timezones
    print("Available Timezones:")
    for index, tz in enumerate(timezones):
        print(f"{index + 1}. {tz}")

    # User selects a timezone
    print("Please enter the number corresponding to your timezone:")
    tz_choice = int(input()) - 1  # User chooses based on 1-based index, adjust to 0-based.
    birth_tz = pytz.timezone(timezones[tz_choice])

    # User input for birthday
    print("Please enter your birthday in the format YYYY-MM-DD HH:MM (e.g., 2000-12-31 23:45)")
    birthdate_str = input("Birthday: ")

    # Get the day of the week
    birth_day = get_birth_day(birthdate_str, birth_tz)
    print(f"You were born on a {birth_day} (probably) !")

if __name__ == "__main__":
    main()
