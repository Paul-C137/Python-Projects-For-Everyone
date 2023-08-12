#!usr/bin/python3

'''This program auto generates a class schedule in the iCal Mac OS app for 
   TLG NDE based on the start date and class start time.  It relies on data 
   stored in a csv file with the following format:

   day offset, minute offset,duration,summary
   0, 30, Greeting
   ...

   Each row in the file represents a block of instruction.
   '''

from datetime import datetime, timedelta
from icalendar import Calendar, Event
import os
import csv

def get_user_input():
    '''Get the start date and time for the course.'''
    date_input = input("Enter the class start date (YYYY-MM-DD): ")
    time_input = input("Enter the class start time (HH:MM): ")
    return date_input, time_input

def create_ical_event(date_str, time_str):
    '''Loops over a csv adding properties to an event object.  Then,
       adds each event object to a calendar object.  Returns the 
       calendar object.'''
    # offset represents the time in minutes we are starting at.
    offset = 0
    day = 0
    # Create calendar object.
    cal = Calendar()
    # Add some necessary things.
    cal.add("version", "2.0")
    cal.add("prodid", "-//My Calendar//EN")
    # Open CSV module.
    with open("tlg_data.csv", "r") as data:
        # Create a reader object with the csv module.
        reader_obj = csv.reader(data)
        #Loop over the csv object.
        for row in reader_obj:
            if row[0] == day:
                # event_date comes from the user.  Add the days offset from the csv.
                event_date = datetime.strptime(date_str, "%Y-%m-%d") + timedelta(days=int(row[0]))
                # event_time comes from the user.  Add the offset value in minutes.
                event_time = datetime.strptime(time_str, "%H:%M") + timedelta(minutes=offset)
                event_start = event_date.replace(hour=event_time.hour, minute=event_time.minute)
                event_end = event_start + timedelta(minutes=int(row[1]))
                event = Event()
                event.add("summary", row[2])
                event.add("dtstart", event_start)
                event.add("dtend", event_end)
                cal.add_component(event)
                offset = offset + int(row[1])
            else:
                day = row[0]
                offset = 0
                # event_date comes from the user.  Add the days offset from the csv.
                event_date = datetime.strptime(date_str, "%Y-%m-%d") + timedelta(days=int(row[0]))
                # event_time comes from the user.  Add the offset value in minutes.
                event_time = datetime.strptime(time_str, "%H:%M") + timedelta(minutes=offset)
                event_start = event_date.replace(hour=event_time.hour, minute=event_time.minute)
                event_end = event_start + timedelta(minutes=int(row[1]))
                event = Event()
                event.add("summary", row[2])
                event.add("dtstart", event_start)
                event.add("dtend", event_end)
                cal.add_component(event)
                offset = offset + int(row[1])
        return cal

def main():
    date_input, time_input = get_user_input()
    cal = create_ical_event(date_input, time_input)
    
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