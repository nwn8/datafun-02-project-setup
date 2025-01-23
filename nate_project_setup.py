"""
Module: nate_project_setup

Purpose: Provide functions to script project folders (and domonstrate basic Python coding skills).

Description: This module provides functions for creating a series of project folders.

Author: Nathan Sloss


"""
#####################################
# Import Modules at the Top
#####################################
import pathlib
import utils_nate
import time
#####################################
# Declare global variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)




#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################


def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''
    
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

    # TODO: Implement the actual folder creation logic
    for year in range(start_year,end_year+1):
        project_path = pathlib.Path.cwd()

        # Create a project data path object
        data_path = project_path.joinpath(f"{year}")

        # Create the data path if it doesn't exist, otherwise do nothing
        data_path.mkdir(exist_ok=True)



#####################################
# Define Function Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################
def create_folders_from_list_one(folder_list: list) -> None:
    '''
    Create folders for a given list of years.
    
    Arguments:
    folder_list = list of years
    '''
    

    print("FUNCTION CALLED: create_folders_from_list_one with folder_list list")
          

    for name in folder_list:
        project_path = pathlib.Path.cwd()

        # Create a project data path object
        data_path = project_path.joinpath(f"{name}")

        # Create the data path if it doesn't exist, otherwise do nothing
        data_path.mkdir(exist_ok=True)


def create_folders_from_list(folder_list: list, to_lowercase: bool, remove_spaces: bool) -> None:
    '''
    Create folders for a given list of years.
    
    Arguments:
    folder_list = list of years
    '''
    

    print("FUNCTION CALLED: create_folders_from_lis with folder_list list")
          

    if to_lowercase:
        folder_list = [x.lower() for x in folder_list]

    if remove_spaces:
        folder_list= [x.replace(" ", "") for x in folder_list]

    for name in folder_list:
        project_path = pathlib.Path.cwd()

        # Create a project data path object
        data_path = project_path.joinpath(f"{name}")

        # Create the data path if it doesn't exist, otherwise do nothing
        data_path.mkdir(exist_ok=True)




#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'data-') to add to each
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    '''
    Create folders for a given list of names adding a prefix of data.
    
    Arguments:
    folder_list = list of years   
    prefix  = string
    '''
    

    print("FUNCTION CALLED: create_prefixed_folders with folder_list and prefix as arguments")
          
    for name in folder_list:
        project_path = pathlib.Path.cwd()

        # Create a project data path object
        data_path = project_path.joinpath(f"{prefix}{name}")

        # Create the data path if it doesn't exist, otherwise do nothing
        data_path.mkdir(exist_ok=True)

#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################



def create_folders_periodically(duration_seconds: int) -> None:
    '''
    Create folders for a given list of names adding a prefix of data.
    
    Arguments:
    duration - integer
    '''
    

    print(f"FUNCTION CALLED: create_folders_periodically every {duration_seconds} seconds")

    total_time = 0
    folder_number = 1

    while total_time < 20:
        # Create a project path object
        project_path = pathlib.Path.cwd()

        # Create a project data path object
        data_path = project_path.joinpath(f"{folder_number}")

        # Create the data path if it doesn't exist, otherwise do nothing
        data_path.mkdir(exist_ok=True)

        folder_number+=1
        total_time+=5

        time.sleep(duration_seconds)


#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
   
    print(f"Byline: {utils_nate.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list_one(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv3', 'excel3', 'json3']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    
    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]

    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()


#TODO: Run this as a script to test that all functions work as intended.
    

