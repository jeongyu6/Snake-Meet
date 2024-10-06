#MODULES TO IMPORT
import csv
import keyboard
from playsound import playsound
import time
import os

def open_file(heat_sheet_filename):
  ''' input: a filename as string
      output: an open file
  '''
  return open(heat_sheet_filename, 'r')

def process_dictionary(file):
  ''' input: an open file
      output: a dictionary with heat names as keys and a list of names as values
  '''
  dictionary = {}  
  file.readline() # column headings
  for line in file:
    l = line.strip().split(',') 
    key = l[0].strip() # heat name (25FL, 50 BK #1 and onwards)
    lanes = l[1:] # names in lanes 1 to 6
    value = [] # empty list for names
    for name in lanes: # removes empty lanes
      if name.strip() != '':
        value.append(name.strip()) #strip to remove any white space
    dictionary[key] = value
  return dictionary

def process_list(dictionary):
  ''' input: a dictionary of heat names
      output: a list of heat names for all races
  '''
  return list(dictionary.keys())

def process_race_names(heat_names):
  ''' input: list of heat names (including all races)
      output: dictionary of race names as keys and heat numbers as values
      the main purpose of this is to create a list of selection for the person to choose from for heat names
  '''
  race_names = {}
  for name in heat_names:
    if name not in race_names:
      if '#' in name:
        index = name.index('#')
        race_name = name[0:index].strip() #25FL or 50BK
        heat_name = name[index+1:].strip() #1, #2, #3
        if race_name not in race_names: #if there is no race name, then put it here
          race_names[race_name] = [heat_name]
        else:                           # if heat name is available, then append it to the race name
          race_names[race_name] = race_names[race_name]+[heat_name]
      else:   # if there is no heat name, just append it into the dictionary
        race_names[name] = []
  return race_names

def heat_chooser(race_name, heat_number, d):
  ''' input: a race name and heat number and a dictionary(d) 
      output: a list of names in that race name and heat number
      example:['Ann','Harry','Kate', 'Lily'] based on the race name and heat number inputted by the user
  '''
  s = race_name
  # a negative 1 as it is impossible to get this number
  if heat_number != -1:
    s = race_name+' #'+heat_number
  return d[s]

def heat_lister(race_name, heat_number):
  ''' input: a race name and heat number and a dictionary 
      output: heat name
  '''
  s = race_name
  if heat_number != -1:
    s = race_name+' #'+heat_number
  return s  


def race_func():
  start_time = input("Press ENTER to start the race ")
  #plays the starting sound
  playsound("Starter Sound.mp3")
  #sets the starting time as 0
  start_time = time.time()
  print ("Press '0' to end the race ")
  #sets the initial results as 0
  race_results = {
      'lane_1': [0],
      'lane_2': [0],
      'lane_3': [0],
      'lane_4': [0],
      'lane_5': [0],
      'lane_6': [0]
  }
  #allows for a keyboard input to set the end time, and  adds to the results. For example, the person presses enter and after a few minutes enters 1,3, and 4. The results records the time intervals of pressing 1,3 and 4 to the starting time.
  while 1 > 0:
    if keyboard.is_pressed('1'):
      #sets the lane's end time to be the time at that moment
      lane1_end = time.time()
      #find the difference between the time of pressing enter to pressing 1
      lane1_time = lane1_end - start_time
      #round off the answer to 3 decimal places
      lane1_time = round(lane1_time, 3)
      print(lane_1_time)
      #adds to the race results to the temporary dictionary
      race_results['lane_1'] = lane1_time
    if keyboard.is_pressed('2'):
      lane2_end = time.time()
      lane2_time = lane2_end - start_time
      lane2_time = round(lane2_time, 3)
      race_results['lane_2'] = lane2_time
    if keyboard.is_pressed('3'):
      lane3_end = time.time()
      lane3_time = lane3_end - start_time
      lane3_time = round(lane3_time, 3)
      race_results['lane_3'] = lane3_time
    if keyboard.is_pressed('4'):
      lane4_end = time.time()
      lane4_time = lane4_end - start_time
      lane4_time = round(lane4_time, 3)
      race_results['lane_4'] = lane4_time
    if keyboard.is_pressed('5'):
      lane5_end = time.time()
      lane5_time = lane5_end - start_time
      lane5_time = round(lane5_time, 3)
      race_results['lane_5'] = lane5_time
    if keyboard.is_pressed('6'):
      lane6_end = time.time()
      lane6_time = lane6_end - start_time
      lane6_time = round(lane6_time, 3)
      race_results['lane_6'] = lane6_time
    if keyboard.is_pressed('q'):
      end_time = time.time()
      end_time_x = end_time - start_time
      end_time_x = round(end_time_x, 3)
      lanes = ['lane_1', 'lane_2', 'lane_3', 'lane_4', 'lane_5', 'lane_6']
      for x in lanes:
        race_results[x] = end_time_x
        
    #the function of 0 stops the recording of the times by using the break function of the keyboard. 
    if keyboard.is_pressed('0'):
      break
    
  lanes = ['lane_1', 'lane_2', 'lane_3', 'lane_4', 'lane_5', 'lane_6']
  race_list = []
  race_list.append(racename)
  #the main purpose of this part of the code is that if a race name does not have a heat number, it will set the heat number as 1
  if one_heat == 1: 
    race_list.append('1') 
  #if it does have a heat number, then it will append that heat number
  else:
    race_list.append(heatname)
  #after getting the results of that heat name and heat number, it will append the results of the times the people took in each of the lane
  for x in lanes:
    race_list.append(race_results[x])
  #it will store the results into a race results dictionary based on the race list for future use.
  race_results_dict[race_heat] = race_list
  return race_results_dict

def csv_transfer(results, final_file):
  #CODE CITATION, took inspiration for this code
    """nikhilaggarwal3, 2019, Writing CSV files in Python, [Code Wiki],
    https://www.geeksforgeeks.org/writing-csv-files-in-python/   
    """
  # field names  
  fields = ['Race Name', 'Heat Number', 'Lane 1', 'Lane 2', 'Lane 3', 'Lane 4', 'Lane 5', 'Lane 6']  
  rows = []    
  # data rows of csv file  
  for x in heats_swam:
    rows.append(results[x])     
  # name of csv file 
  # writing to csv file  
  with open(final_file, 'w') as csvfile:  
      # creating a csv writer object  
      csvwriter = csv.writer(csvfile)   
      # writing the fields: aims to place the header of race name, heat number and so on on top. 
      csvwriter.writerow(fields)   
      # writing the data rows: this is to place the values below each header: for example, we have ['25 FL','1',2.49,[0] and so on]  
      csvwriter.writerows(rows)    
  return csvfile  

#Initial variable values
# _name_ = 0
if __name__ == "__main__":
  menu_option = ''
  menu_string = ''
  file = ''
  file_input = ''
  filename = ''
  heat_names = []
  race_dict = {}
  dictionary = []
  race_list = []
  race_results_dict = {}
  heats_swam = []
  final = ''
  race_heat = ''
  one_heat = 0
  
  print("\nWelcome to SnakeMeet2023")
  while (menu_option != 'E'):
    print('--------------------------')
    print('Menu:')
    A = print("[Option A] Select a file")
    B = print("[Option B] Choose race and heat")
    C = print("[Option C] Start the race")
    D = print("[Option D] Transfer to CSV file")
    E = print("[Option E] Exit software")
    V = print("[Option V] Version information")
    print('--------------------------')
    menu_option = input("Select a menu option: \n >>> ")
    #placing .upper() to convert user's input of small letters to capital letters
    menu_option = menu_option.upper()
    if (menu_option == "A"):
      file_input = input("What is the name of the heat file for the race? \n >>> ")
      #os.path.isfile() is a function to check if it is an existing file and if it is, it returns the boolean statement true. 
      #Otherwise, it is false. This ensures that there is no problem in the file while processing
      if os.path.isfile(file_input):
        #let the user open the file
        file = (open_file(file_input))
        #let the user open up a dictionary of the file
        dictionary = process_dictionary(file)
        #process the heat names from the dictionary
        heat_names = process_list(dictionary)
        #connect race names to heat_names
        race_dict = process_race_names(heat_names)
        print('Files opened successfully')        
      else:
        print ("You have entered an invalid file")

    elif (menu_option == "B"):
      #Ensuring that a file has been opened before starting the code. Use if and else statement to ask the user to put the file
      if file != '':
        i = 0 
        print('--------------------------')
        print('Race Names:')
        #provides the user options for the race names from 1 to a specific number of races available in the dictionary
        #It uses an elemental for loop to allow the user to see the options ranging from 1 onwards.
        #we placed str(i+1) as i would technically start from 0 and we want options to range from 1 onwards. 
        for race in race_dict:
          print('[Option '+str(i+1)+']', race)
          i += 1
        print('--------------------------')      
        user_input1 = input("Select a race name: \n >>> ")
        #Making sure that the user input is a number. This is by using isdigit()
        if user_input1.isdigit():
        #the person can only put a number less than the available numbers or should be greater than 0 to be valid. 
          if int(user_input1) <= i and int(user_input1)>0:
            i = 0
            #as the index only starts at 0 in python, we have to select the racename by subtracting 1
            racename = list(race_dict.keys())[(int(user_input1))-1]
            #some race names have a heat name. For those, they do not have an empty list. So, we placed if it is not equal to an empty list, this follows
            if race_dict[racename] != []:
              print('--------------------------')   
              print('Heat Numbers:')
              #This is for the heat numbers from 1-3 available or smaller.
              for heat in race_dict[racename]:
                print('[Option '+str(i+1)+']', heat)
                i += 1
              print('--------------------------')
              user_input2 = input("Select a heat number: \n >>> ")
              if int(user_input2) <= i and int(user_input2)>0:
                heatname = race_dict[racename][(int(user_input2))-1]
                print('\n')
                print('The racers in', racename, '#', heatname,'are:')
                #Heat Chooser=names. It will print it where the name 1',' name2',' name 3','and so on. The join function is for separating the names using commas easily.
                print(', '.join(heat_chooser(racename, heatname, dictionary)))
                print('\n')
                race_heat = heat_lister(racename, heatname)
                #adds an order list of the races that was selected already
                #one_heat=0 is false because there is a heat name. 
                one_heat = 0
                heats_swam.append(race_heat)
              else:
                print ("You have entered an invalid heat number")
            else:
              print('\n')
              print('The racers in', racename, 'are:')
              #add -1 as we would never get a -1 racename
              print(', '.join(heat_chooser(racename, -1, dictionary)))
              print('\n')
              heatname = 1
              #one_heat is true when there is no heat name. 
              one_heat = 1
              race_heat = racename
              heats_swam.append(racename)
          else:
            print ("You have entered an invalid race number")
        else:
          print ("You have entered an invalid race number")
      else:
        print ("Please enter a heat file before continuing")
    elif (menu_option == "C"):
      #making sure there is a race selected, otherwise CSV file does not work
      if race_heat != '':
        race_func()
        print ('Race Completed')
      else:
        print ("Please select a race and heat before continuing")
      #fixes a bug where the 0 key was pressed for too long
      keyboard.press("backspace")
      keyboard.restore_state([])
    elif (menu_option == "D"):
      if race_results_dict != {}:
        filename = input("Please input the results file: \n >>> ")
        #ensures the file is actually a file by using os.path.isfile
        if os.path.isfile(filename):
          final = csv_transfer(race_results_dict, filename)
          print ('Data Transfer Sucessful')                
        else:
          print ("You have entered an invalid file")
      else:
        print ("Please run at least one race before transfering data")
    elif (menu_option == "E"):
      print ("Thank you for using SnakeMeet2023")
      break
    elif (menu_option == "V"):
      print(
      '''
      Version Number: 1.0.0
      Company Name: SnakeMeet2023
      ''')
    else:
      print ("You have entered an invalid option")

#final checks to make sure that just starting and exiting the software
#does not crash it
if os.path.isfile(file_input):
  file.close
if os.path.isfile(filename):
  final.close