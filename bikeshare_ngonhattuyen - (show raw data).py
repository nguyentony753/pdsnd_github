########################################################################
# Author: Tuyen Ngo Nhat
# Create On: Mar/25/2023 
# Version : v1.1
# Description : Everything is so lucky, good, healthy
# Udacity : Programming for Data Science with Python 
# Project II : Explore US Bikeshare Data
########################################################################


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\n Please select the city you want to filter? chicago, new york city, washington\n")
        if city not in ('chicago', 'new york city', 'washington'):    
            print("Sorry.I can't do the filtering, please try again")
            continue
        else:
            break
        
        
    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
       month = input("\n Please select the month you want to filter? January, February, March, April, May, June or Type 'all' if you don't have any preference?\n")
       if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
            print("Sorry.I can't do the filtering, please try again.")
            continue
       else:
            break
        
       
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        day = input("\n Please select the month you want to filter? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you do not have any preference.\n")
        if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
            print("Sorry.I can't do the filtering, please try again.")
            continue
        else:
            break  
            
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # We Load Data File Into A Data Frame
    df = pd.read_csv(CITY_DATA[city])

    
    # We Convert The Start Time Column To Datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    
    # We Extract Month And Day Of Week From Start Time To New Colume
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    
    # We Filter By Month
    if month != 'All':
      # We Use The Index Of The Month List To Get The Corresponding Int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
      # We Filter By Month To Create The New Data Frame
        df = df[df['month'] == month]
        
        # Filter By Day Of Woeek If Applicable
    if day != 'All':
        
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)
                                       

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day)
                                       

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common day:', popular_hour)
                                                             

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('MOst Commonly Used Start Station:', Start_Station)
                                       

    # TO DO: display most commonly used end station
    End_Station = df['Start Station'].value_counts().idxmax()
    print('MOst Commonly Used Start Station:', End_Station)
                                       

    # TO DO: display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nThe Most Frequent Combination Of Start Station And End Station Trip:', Start_Station, " & ", End_Station )
                                       
                             
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total Travel Time:', Total_Travel_Time/86400, " Days")
    

    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean Travel Time:', Mean_Travel_Time/60, " Minutes")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('User Types:\n', user_types)

    
    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")
    

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        Earliest_Year = df['Birth Year'].min()
        print('\nEarliest Year:', Earliest_Year)
    except KeyError:
        print("\nEarliest Year:\nNo Data Available For This Month.")
        
        
    try:
        Most_Recent_Year = df['Birth Year'].max()
        print('\nMost Recent Year:', Earliest_Year)
    except KeyError:
        print("\nMost Recent Year:\nNo Data Available For This Month.")      
 

    try:
        Most_Common_Year = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year:', Earliest_Year)
    except KeyError:
        print("\nMost Common Year:\nNo Data Available For This Month.") 
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    

def display_data(df):
    # to prompt the user wether he like to display the raw data of that city as chunks of 5 row based upon user input.
    print('\nRaw data is available to check... \n')
    
    index=0
    user_input=input('Choose yes or no if you want to display raw data or not ').lower()
    if user_input not in ['yes','no']:
        print('That\'s invalid choise, please type yes or no')
        user_input=input('Choose yes or no if you want to display raw data or not ').lower()
    elif user_input != 'yes':
        print('Thank!')
    else:
        while index+5 < df.shape[0]:
            print(df.iloc[index:index+5])
            index += 5
            user_input = input('would you like to display more 5 rows of raw data? ').lower()
            if user_input != 'yes':
                print('Thank!')
                break
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
                         
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
