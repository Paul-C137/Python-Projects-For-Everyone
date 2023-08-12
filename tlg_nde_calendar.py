from datetime import datetime, timedelta
from icalendar import Calendar, Event
import os

def get_user_input():
    date_input = input("Enter the class start date (YYYY-MM-DD): ")
    return date_input

def create_ical_event(date_str):
    event_date = datetime.strptime(date_str, "%Y-%m-%d")
    event_time = datetime.strptime("08:00", "%H:%M")
    event_start = event_date.replace(hour=event_time.hour, minute=event_time.minute)
    event_end = event_start + timedelta(minutes=30)
    event_0 = Event()
    event_0.add("summary", "Greeting")
    event_0.add("dtstart", event_start)
    event_0.add("dtend", event_end)

    event_time = event_time + timedelta(minutes=30)
    event_start = event_date.replace(hour=event_time.hour, minute=event_time.minute)
    event_end = event_start + timedelta(minutes=30)
    event_1 = Event()
    event_1.add("summary", "Lab 1: Welcome to Alta3 Research Labs")
    event_1.add("dtstart", event_start)
    event_1.add("dtend", event_end)
    return event_0, event_1

def main():
    date_input = get_user_input()
    event_0, event_1 = create_ical_event(date_input)
    
    cal = Calendar()
    cal.add("version", "2.0")
    cal.add("prodid", "-//My Calendar//EN")
    
    cal.add_component(event_0)
    cal.add_component(event_1)
    
    # Save the event to a file
    event_filename = "event.ics"
    with open(event_filename, "wb") as f:
        f.write(cal.to_ical())
    
    # Run AppleScript to add the event to macOS Calendar app
    script = f'do shell script "open -a Calendar {event_filename}"'
    os.system(f"osascript -e '{script}'")
    
    print("Event created and added to macOS Calendar app")

if __name__ == "__main__":
    main()