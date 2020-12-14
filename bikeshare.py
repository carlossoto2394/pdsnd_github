import time
import pandas as pd
import numpy as np

## Dictionaries
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

valid_months= ('all','january','february','march','april','may','june') 
valid_days= ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday') 

MONTHS = { 'january': 1,'february': 2,'march': 3,'april': 4,'may': 5,'june': 6}
MONTHS_name = { 1: 'january',2: 'february',3: 'march',4:'april',5:'may',6:'june'}

DAYS = { 'monday': 0,'tuesday': 1,'wednesday': 2,'thursday': 3,'friday': 4,'saturday': 5,'sunday': 6}                   
DAYS_name = { 0: 'monday',1: 'tuesday',2: 'wednesday',3: 'thursday',4: 'friday',5: 'saturday',6: 'sunday'} 

cities_with_userinfo= ('chicago','new york city') 

## Welcome Message
print('Hello! Let\'s explore some US bikeshare data!')

def get_filters():
#    """
#    Asks user to specify a city, month, and day to analyze.

#    Returns:
#        (str) city - name of the city to analyze
#        (str) month - name of the month to filter by, or "all" to apply no month filter
#        (str) day - name of the day of week to filter by, or "all" to apply no day filter
#    """

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
  
    while True: 
        input_city=str(input('please select the city that you want to study - chicago, new york city or washington :     ').lower())

        if input_city in CITY_DATA:
            city_= True
        else: 
            print("invalid input")
            continue

        break
       
    # TO DO: get user input for month (all, january, february, ... , june)
    while True: 
        input_month=str(input('please select a month, or all months to study - (all, january, february, ... , june) :     ').lower())

        if input_month in valid_months:
            month_= True
        else: 
            print("invalid input")
            continue

        break
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True: 
        input_day=str(input('please select a day, or all days to study - (all, monday, tuesday, ... sunday) :     ').lower())

        if input_day in valid_days:
            day_= True
        else: 
            print("invalid input")
            continue

        break

    print('-'*40)
    return { 'city': input_city,
              'month': input_month,
              'day': input_day }

#filters=get_filters()



def load_data(city, month, day):
#    """
#    Loads data for the specified city and filters by month and day if applicable.

#    Args:
#        (str) city - name of the city to analyze
#        (str) month - name of the month to filter by, or "all" to apply no month filter
#        (str) day - name of the day of week to filter by, or "all" to apply no day filter
#    Returns:
#        df - Pandas DataFrame containing city data filtered by month and day
#   """

    with open(CITY_DATA[city],'r') as city:
            data_city = pd.read_csv(city)
    data_city['Start Time']=pd.to_datetime(data_city['Start Time'])
    
    filtered_data=data_city
    
    if month == 'all' and day == 'all':
        return filtered_data
    elif month == 'all' and day != 'all':
        filtered_data = filtered_data[filtered_data['Start Time'].dt.weekday == DAYS[day]]
    elif month !='all' and day == 'all':
        filtered_data = filtered_data['Start Time'].map(lambda x: x.month) == MONTHS[month]
    elif month !='all' and day !='all':
        filtered_data = filtered_data[(filtered_data['Start Time'].dt.weekday == DAYS[day]) & (filtered_data['Start Time'].dt.month == MONTHS[month])]
        
     
    return filtered_data

#loaded_data=load_data(filters['city'],filters['month'],filters['day'])


def time_stats(data_city):
#    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    
    st_city = data_city['Start Time']
    st_city = pd.to_datetime(st_city)
    date_st_city= pd.to_datetime(st_city).dt.date
    month_st_city= pd.to_datetime(st_city).dt.month
    day_st_city= pd.to_datetime(st_city).dt.day
    time_st_city= pd.to_datetime(st_city).dt.time
    weekday_st_city=pd.to_datetime(st_city).dt.weekday
  
     
      
    
    # TO DO: display the most common month
    print('the most common month taking bikes is:  ',MONTHS_name[month_st_city.mode()[0]])

    # TO DO: display the most common day of week
    print('the most common day of the week taking bikes is:  ',DAYS_name[weekday_st_city.mode()[0]])

    # TO DO: display the most common start hour
    print('the most common time taking bikes is:  ',time_st_city.mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#time_stats(loaded_data)
    
def station_stats(data_city):
  
    ss_city = data_city['Start Station']
    es_city = data_city['End Station']
    r_city = ss_city +'--' + es_city
   
    
#    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('the most common start station is:   ',ss_city.mode())

    # TO DO: display most commonly used end station
    print('the most common end station is:   ',es_city.mode())     

    # TO DO: display most frequent combination of start station and end station trip
    print('the most common frequent combination of start station and end station trip is:   ',r_city.mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(data_city,test_info):
    td_city = data_city['Trip Duration']
    ut_city = data_city['User Type']
    if test_info== True:
        g_city = data_city['Gender']
        by_city = data_city['Birth Year']

       
#    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('the total travel time is:  ',td_city.sum())

    # TO DO: display mean travel time
    print('the mean travel time is:  ',td_city.mean())
    
    # display mean travel time over user type
    print('mean travel time over user type')
    print(td_city.groupby(ut_city).mean())
    
    # display mean travel time over gender, and birth year
    if test_info== True:
           print('mean travel time over gender and birth year')
           print(td_city.groupby(g_city).mean())
           print(td_city.groupby(by_city).mean())
           

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(data_city,test_info):
    ut_city = data_city['User Type']
    if test_info== True:
        g_city = data_city['Gender']
        by_city = data_city['Birth Year']
    
#    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(ut_city.value_counts())

    # TO DO: Display counts of gender
    if test_info== True:
        print(g_city.value_counts()) 

    # TO DO: Display earliest, most recent, and most common year of birth
    if test_info== True:
        print('the earliest birth year is: ',by_city.min())
        print('the most recent birth year is: ',by_city.max())
        print('the most common year of birth is: ',by_city.mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

## Main Function
def main():
    while True:
        filters = get_filters()
        df = load_data(filters['city'],filters['month'],filters['day'])

        #print optinal raw data
        x=0# first counter
        y=5# second counter
        while True:
          input_rawdata = str(input("Do you want to see raw data?: yes or no?  ").lower())
            
          if input_rawdata == "yes":
            print(df.iloc[x:y])
            x=x+5
            y=y+5

          else:# if no get out of loop
            break
        
        
        time_stats(df)
        station_stats(df)
        
        g_city=None
        by_city=None
        user_info=None
        
        if filters['city'] in cities_with_userinfo:
            g_city = df['Gender']
            by_city = df['Birth Year']
            user_info= True
                
        
        trip_duration_stats(df,user_info)
        user_stats(df,user_info)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()