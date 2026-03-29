import pandas as pd

birthdays_df=d.read_csv('birthdays.csv')

#print the content
print("Current Birthdays in the Calender:")
print(birthdays_df)

#Add new birthday to the calender
new_birth ={'Name': 'Matthew', 'Date': '2024-2-15'}
birthdays_df = birthdays_df.append(new_birthday, ignore_index=True)

#Save the updatd file back ti the CSV 
birthdays_df.to_csv('birthdays.csv', index=False)
print("Successfully added Matthew's birthday to birthdays.csv and saved the updated file.") 
