# importing packages to be used
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

categories = { '1': 'Popular Travel Times',
               '2': 'Popular Stations and Trips',
               '3': 'Trip Durations',
               '4': 'User Info',
               '5': 'Raw Data' }

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data! ')

    city = str(input('\nWhich city would you like to see data for? Chicago, Washington, or New York City? '))

    while city.lower() not in CITY_DATA:
        city = str(input('\nWhoops, try again. Chicago, Washington, or New York City? '))

    category = str(input('\nWhat statistics are you looking for? \n\nEnter "1" for Popular Travel Times, \n"2" for Popular Stations and Trips, \n"3" for Trip Duration, \n"4" for User Info, or \n"5" for Raw Data. '))

    while category not in categories:
        category = str(input('\nThat\'s not a category, try again! \n\nEnter "1" for Popular Travel Times, \n"2" for Popular Stations and Trips, \n"3" for Trip Durations, \n"4" for User Info, or \n"5" for Raw Data. '))

    print('-'*40)
    return city, category

# Load data from city's csv
def load_data(city, category):
    df = pd.read_csv(CITY_DATA[city.lower()])

    return df

# Category1, time stats
def time_stats(df):

    print('\nCalculating The Most Popular Travel Times...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    busiest_month = df['month'].mode()[0]
    busiest_day_of_week = df['day_of_week'].mode()[0]
    busiest_hour_of_day = df['hour'].mode()[0]

    print('Busiest month: ', busiest_month)
    print('Busiest day of the week: ', busiest_day_of_week)
    print('Busiest hour of the day: ', busiest_hour_of_day)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Category2, station stats
def station_stats(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    popular_start_station = df['Start Station'].mode()[0]
    popular_end_station = df['End Station'].mode()[0]
    df['Station Combination'] = 'From ' + df['Start Station'].map(str) + ' to ' + df['End Station']
    popular_start_end = df['Station Combination'].value_counts().idxmax()

    print('Most popular start station: ', popular_start_station)
    print('Most popular end station: ', popular_end_station)
    print('Most popular trip: ', popular_start_end)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Category3, trip duration stats
def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = float(df['Trip Duration'].sum())
    avg_travel_time = float(df['Trip Duration'].mean())

    print('Total travel time: ', total_travel_time / (60 * 60 * 24 * 365.25), 'years')
    print('Average travel time: ', avg_travel_time / 60, 'minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Category4, user stats
def user_stats(city, df):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print(user_types)

    if city.lower() == "washington":
        print('No age or gender data is available for this city. ')
    elif city.lower() == "chicago" or "new york city":
        user_genders = df['Gender'].value_counts()
        earliest_birth_year = int(df['Birth Year'].min())
        latest_birth_year = int(df['Birth Year'].max())
        common_birth_year = int(df['Birth Year'].mode()[0])
        print(user_genders)
        print('\nEarliest Birth Year: ', earliest_birth_year)
        print('Latest Birth Year: ', latest_birth_year)
        print('Most Common Birth Year: ', common_birth_year)
    else:
        print('Could you try that again? ')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Category5, raw data
def raw_data(city, df):

    print('\nGathering Raw Data...\n')
    start_time = time.time()

    print('Here\'s the first 5 rows for {}.\n'.format(city.title()))
    print(df.head())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    i = 5
    raw_data_response = str(input('Would you like to see 5 more rows? Enter yes or no. '))

    while raw_data_response.lower() == 'yes':
        i += 5
        print(df.head(i))
        print('-'*40)
        raw_data_response = str(input('Would you like to see 5 more rows? Enter yes or no. '))


# main block
def main():
    while True:
        city, category = get_filters()
        df = load_data(city, category)

        if category == '1':
            time_stats(df)
        elif category == '2':
            station_stats(df)
        elif category == '3':
            trip_duration_stats(df)
        elif category == '4':
            user_stats(city, df)
        else:
            raw_data(city, df)

        restart = input('\nWould you like start another search? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
