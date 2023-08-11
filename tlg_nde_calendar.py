from datetime import datetime, timedelta
from icalendar import Calendar, Event
import os

def get_user_input():
    date_input = input("Enter the date (YYYY-MM-DD): ")
    time_input = input("Enter the time (HH:MM): ")
    return date_input, time_input

def create_ical_event(date_str, time_str):
    event_date = datetime.strptime(date_str, "%Y-%m-%d")
    event_time = datetime.strptime(time_str, "%H:%M")
    event_start = event_date.replace(hour=event_time.hour, minute=event_time.minute)
    event_end = event_start + timedelta(minutes=30)
    
    event = Event()
    event.add("summary", "test")
    event.add("dtstart", event_start)
    event.add("dtend", event_end)
    
    return event

def main():
    date_input, time_input = get_user_input()
    event = create_ical_event(date_input, time_input)
    
    cal = Calendar()
    cal.add("version", "2.0")
    cal.add("prodid", "-//My Calendar//EN")
    
    cal.add_component(event)
    
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