from bs4 import BeautifulSoup
import json
import requests

target_ip = 'adapter'
target_port = 20001
url = f'http://{target_ip}:{target_port}'
headers = {
    'Content-Type': 'application/json'
}
final_list=[]

def search_inmates():
# Create the final list to return later.
# Request data and create soup object.
    source = requests.get \
    ('https://www.skagitcounty.net/Reporting/JailRoster/').text
    #source = httpx.get('https://www.skagitcounty.net/Reporting/JailRoster/').content
    soup = BeautifulSoup(source, 'lxml') 
# Create a list to parse soup object's strings into.
    my_list = []
# Find text in the soup object with the info we want and insert into a list.
    for x in soup.find_all("td", nowrap = 'nowrap'):
        for index, item in enumerate(x):
            my_list.insert(index, x.text) 
# The list is backwards so we have to flip it around into a new list.
    length = len(my_list)       
    new_list = []
    for index, item in enumerate(my_list):
            new_list.insert(index, my_list[length-1-index])

# The new_list contains some seriously long and unecessary text elements.  By 
# getting rid of everything over 30 characters long, we clean our list and
# make sure every single key has the exact same values.
    clean_list = []
    for index, item in enumerate(new_list):
        if (len(item)) < 30:
            clean_list.insert(index, new_list[index])
        
# Iterate the list and check for elements that can be converted to integers.
# These elements are the inmate's name number.
    for index, item in enumerate(clean_list):
        count = 0
        if item.isnumeric():
# If it can be converted, change it to an int and check if it is legitimate.
# Name numbers can be from 1 to 999999.
# Nobody realistically has a name number below 999.
            if int(item) > 999 and int(item) < 999999:
# The 4 elements before the name number are always inmate name data.
# We have to check if all or some exist by checking the element for caps.
# Fill in the inmate dictionary with the appropriate data depending on the
# number of 'name' elements we found preceeding the name number.  
                for i in range(1,5):
                    if clean_list[index-i].isupper():
                        count = count+1
        if count == 2:
            final_list.append([clean_list[index],clean_list[index-count],\
            clean_list[index-count+1],'','', clean_list[index+6],\
            clean_list[index+2][8:17], clean_list[index+2][8:17]])
        elif count == 3:
            final_list.append([clean_list[index],clean_list[index-count],\
            clean_list[index-count+1], clean_list[index-count+2],'',\
            clean_list[index+6], clean_list[index+2][8:17],\
            clean_list[index+2][8:17]])
        elif count == 4:
            final_list.append([clean_list[index],clean_list[index-count],\
            clean_list[index-count+1], clean_list[index-count+2],\
            clean_list[index-count+3], clean_list[index+6],\
            clean_list[index+2][8:17], clean_list[index+4][2:17]])

# List structure:  Name Number of inmate, Last, First, Middle, Suffix, 
# Housing Location, Date of Arrest
    return final_list, clean_list

def convert_to_list_of_dict(inmates):
    d=[]
    for inmate in inmates:
       inmate_dict = {'name_number': inmate[0], 'last_name': inmate[1], 'first_name': inmate[2], 'middle_name': inmate[3], 'suffix': inmate[4], 'location': inmate[5], 'incarceration_date': inmate[6]}
       d.append(inmate_dict)
    return d

inmates, clean_list = search_inmates()
inmates_converted = convert_to_list_of_dict(inmates)
print(inmates_converted)
