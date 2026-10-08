#Mini project - Contact book. List of dictionaries
contacts = [ {'name': 'Kevin Kimee', 'phone_no': '0711121314' , 'city': 'Bomet', 'skill': 'Masonry'},
{'name': 'Godish Cherotich', 'phone_no': '0716171819', 'city': 'Kericho', 'skill':'Welding'},
{'name': 'Delvine Mutai', 'phone_no': '0720212224', 'city': 'Konoin', 'skill': 'Carpenter'},
{'name': 'Lenox Kibet' , 'phone_no': '0725262728', 'city': 'Bomet', 'skill': 'Farming'},
{'name': 'Kiptelwa Koech', 'phone_no': '0729303132', 'city': 'Bomet', 'skill': 'Catering'},
{'name': 'Grace Njenga', 'phone_no': '0733343536', 'city': 'Nakuru', 'skill': 'Welding'}]

#Displaying contacts neatly.
print("===== CONTACT BOOK =====")
for i, contact in enumerate(contacts):
    print(f"\n{i+1}. {contact['name']}")
    print(f"     Phone : {contact['phone_no']}")
    print(f"     Skill : {contact['skill']}")
    print(f"     City : {contact['city']}")
    
    
print('\n')
#Searching the contact
search_name = 'Lenox Kibet'    
found = False
for contact in contacts:
    if contact['name'] == search_name:
        print('The contact was found')
        print(f"Name: {contact['name']}")
        print(f"  Skill  : {contact['skill']}")
        print(f"  Phone  : {contact['phone_no']}")
        print(f"  City  : {contact['city']}")
        found = True
        break
if not found:
     print("No contact found with name:", search_name)     
     
print('\n')
#Searching by City.
search_city = 'Bomet'  
print (f'Contacts in {search_city}')
for contact in contacts:
    if contact['city'] == search_city:
        print(f"  {contact['name']} with skill in  {contact['skill']} and the contact is {contact['phone_no']}")
        print('\n')
        
#Adding a new contact
print("Before:", len(contacts), "contacts") 
new_contact = {'name': 'Daniel' , 'phone_no': '0741424344', 'city': 'Bomet', 'skill': 'Tailoring'}
contacts.append(new_contact)
print("\nAfter:", len(contacts), "contacts")

print('\n=====END OF CONTACT BOOK=====')
 
