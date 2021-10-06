from datetime import datetime
import requests
import json
import time
import os

def logo():
    print('  _____                    _  _  _   __        _____                                      _    _                     __      __   ___     ___    __ ')
    print(' / ____|                  | || |(_) / _|      |  __ \                                    | |  (_)                    \ \    / /  / _ \   / _ \  /_ |')
    print('| |  __   ___    ___    __| || | _ | |_  ___  | |__) | ___  ___   ___  _ __ __   __ __ _ | |_  _   ___   _ __   ___   \ \  / /  | | | | | | | |  | |')
    print('| | |_ | / _ \  / _ \  / _` || || ||  _|/ _ \ |  _  / / _ \/ __| / _ \| \'__|\ \ / // _` || __|| | / _ \ | \'_ \ / __|   \ \/ /   | | | | | | | |  | |')
    print('| |__| || (_) || (_) || (_| || || || | |  __/ | | \ \|  __/\__ \|  __/| |    \ V /| (_| || |_ | || (_) || | | |\__ \    \  /    | |_| |_| |_| |_ | |')
    print(' \_____| \___/  \___/  \__,_||_||_||_|  \___| |_|  \_\\\\___||___/ \___||_|     \_/  \__,_| \__||_| \___/ |_| |_||___/     \/      \___/(_)\___/(_)|_|')
    print('                     Built by Xhrbes#1234                    ')

logo()




site_url ='http://2captcha.com/in.php?key=[YOUR 2CAP TOKEN HERE]&method=userrecaptcha&googlekey=6Lfz3I8aAAAAACbq6gVz0yzf9__GZcUmqqdp8WHt&json=1&pageurl=https://www.goodlifefitness.com/Goodlifelogin.html'
user_Date = str(datetime.date(datetime.now()))
s = requests.Session()
captcha = s.post(site_url)
captcha = json.loads(captcha.text)

captcha_id = captcha['request']
site_urlv2 = 'http://2captcha.com/res.php?key=[YOUR 2CAP TOKEN HERE]&json=1&action=get&id=' + str(captcha_id)
r = s.post('https://www.goodlifefitness.com/content/experience-fragments/goodlife/header/master/jcr:content/root/responsivegrid/header.Update_Last_Login.json')
ping = r
print(r.text)

captcha = s.get(site_urlv2)
response = json.loads(captcha.text)



count = 0
start = time.time()
while response['request'] == 'CAPCHA_NOT_READY':
    count = count + 1

    captcha = s.get(site_urlv2)
    response = json.loads(captcha.text)
    if count % 5 == 0:
        print('Awaiting  Captcha Solver... [' + str(count//5) + ']')
end = time.time()


captcha_webhook = 'INSERT YOUR OWN DISCORD WEBHOOK FOR FUNTIONALITY' 
captcha_stats = {
            'username':'Goodlife Captcha Solves'
        }
captcha_stats['embeds'] = [
    {
        'title':'Captcha V2',
        'fields':[{
            'name':'Time Taken to Solve',
            'value':str(end - start)
        }]

}]

captcha_webhook = requests.post(captcha_webhook, json=captcha_stats)

print('Captcha Tokens Found!'+ '| Time Taken to Solve : ' + str(end - start))    
captcha_token = response['request']

print('Checking Goodlife Site Status...')

r = s.get('https://www.goodlifefitness.com/home.html')
ping = r
if '<Response [200]>' == str(ping):
    print('\nSTATUS OK')
    time.sleep(3)

email = input('Enter Goodlife Account Email : ')
password = input('Enter Goodlife Account Password : ')
Formdata = {'login':email, 'passwordParameter':password, 'captchaToken':captcha_token}
print(s.cookies)
r = s.post('https://www.goodlifefitness.com/content/experience-fragments/goodlife/header/master/jcr:content/root/responsivegrid/header.AuthenticateMember.json', data=Formdata)
ping = r
if '<Response [200]>' == str(ping):
    print('Logging in...')
    print(r.text)
else:
    print('Error Logging in!')
    print(r.text)

r = s.post('https://www.goodlifefitness.com/content/experience-fragments/goodlife/header/master/jcr:content/root/responsivegrid/header.Update_Last_Login.json')
ping = r
if '<Response [200]>' == str(ping):
    print('Successfully Logged in!')
    print(r.text)


print(s.cookies)
time.sleep(5)

r = requests.get('https://www.goodlifefitness.com/content/goodlife/en/book-workout/jcr:content/root/responsivegrid/workoutbooking.GetMemberWorkoutBookings.' + user_Date + '.json')
ping = r
if '<Response [200]>' == str(ping):
    print('Retrieving Schedule...')
    time.sleep(1)
    os.system('cls')


r = s.post('https://www.goodlifefitness.com/content/experience-fragments/goodlife/header/master/jcr:content/root/responsivegrid/header.Update_Last_Login.json')
ping = r
print(r.text)

#This is where the GoodLife loads the clubs from. You must ping from a location relatively near your desired club using longitude and latitude.
r = requests.get('https://www.goodlifefitness.com/content/experience-fragments/goodlife/header/master/jcr:content/root/responsivegrid/header.GetClosestClub.(Longitude).(latitude)..(date in yyyy-mm-dd format).json')
club_list = json.loads(r.text)
r.close()
clubs = club_list['map']['response']
#print(clubs)
logo()
userinput = str(input('\nEnter the Club Location : '))
userinput = userinput.split(' ')
os.system('cls')
logo()
print('\nRetrieving Clubs...')
time.sleep(1)
for club in clubs:
    #print(club['ClubName'] + ' Club ID : ' + str(club['ClubNumber']) + '\n')
    #print(club['Gender'] +  ' Location Status : ' + str(club['IsOpen']))
    count = 0 
    for kws in range(len(userinput)):
        if count == len(userinput):
            break
        elif userinput[kws] in club['ClubName']:
            print('Filtering Results...')
            os.system('cls')
            count = count + 1
    if count == len(userinput):
        clubName = club['ClubName']
        clubId = str(club['ClubNumber'])
        #print(clubName + ' | ' + clubId)
        break











r = requests.get('https://www.goodlifefitness.com/content/goodlife/en/book-workout/jcr:content/root/responsivegrid/workoutbooking.GetWorkoutSlots.' + clubId + '.' + user_Date + '.' + 'json')
logo()
ping = r
if '<Response [200]>' == str(ping):
    print('\nSuccessfully Extracted Schedule!')
    print('Generating...')
    time.sleep(2)
    os.system('cls')


workoutList = json.loads(r.text)
#print(workoutList)
workouts = workoutList['map']['response']
#print(workouts)
#print(workouts)
for workoutdays in range(len(workouts)):
    for workout in workouts[workoutdays]['workouts']:
        if workout['gymArea'] == 'For Women':
            print('Day : ' + workout['dayOfWeek'] + ' | Time slot : ' + workout['startDateObj'] +  ' to ' + workout['endDateObj'] + ' | WOMENS ONLY')
            print('Total Capacity : ' + str(workout['maxOccupancy']) + ' | Current Capacity : ' + str(workout['currentOccupancy']) + ' | Available Slots : ' + str(workout['availableSlots']) + '\n')
        else:
            print('Day : ' + workout['dayOfWeek'] + ' | Time slot : ' + workout['startDateObj'] +  ' to ' + workout['endDateObj'] + ' | COED')
            print('Total Capacity : ' + str(workout['maxOccupancy']) + ' | Current Capacity : ' + str(workout['currentOccupancy']) + ' | Available Slots : ' + str(workout['availableSlots']) + '\n')

r = s.post('https://www.goodlifefitness.com/content/experience-fragments/goodlife/header/master/jcr:content/root/responsivegrid/header.Update_Last_Login.json')
ping = r
print(r.text)


DateInput = input('Enter Date of Workout *YY-MM-DD Format* : ')
DateInput = DateInput.split('-')
timeInput = input('Enter Time Slot *Military Time Format* : ')
timeInput = timeInput.split(':')
userGender = input('Male or Female : ')

if userGender == 'Female':
    genderFilter = 'For Women'
elif userGender == 'Male':
    genderFilter = 'Gym Floor'
print('Filtering Results....')
print(genderFilter)
time.sleep(1)
os.system('cls')
for workoutdays in range(len(workouts)):
    #for workout in :
    #print(workouts[workoutdays])
    for workout in workouts[workoutdays]['workouts']:
        timeSlot = workout['startDateObj'].split('T')
        timeSlot = timeSlot[-1].split(':')
        slotDate = workout['dayOfWeek'].split('T')
        slotDate = slotDate[0].split('-')
        #print(slotDate)
        #print(timeSlot)
        #print('Day : ' + workout['dayOfWeek'] + ' | Time slot : ' + workout['startDateObj'] +  ' to ' + workout['endDateObj'] + ' | ID : ' + str(workout['identifier']))
       # print('Total Capacity : ' + str(workout['maxOccupancy']) + ' | Current Capacity : ' + str(workout['currentOccupancy']) + ' | Available Slots : ' + str(workout['availableSlots']) + '\n')
        count = 0
        countv2 = 0
        for slotTime in range(len(slotDate)):

            if DateInput[slotTime] in slotDate:
                count = count + 1
                print('Filtering Results...')
                os.system('cls')
                #print(count)
            if count == len(slotDate):
                print('Detected Kws!')
                os.system('cls')
                #countv2 = 0
                for slotSchedule in range(len(timeSlot)):
                    if countv2 == len(timeSlot):
                        break

                    elif timeInput[slotSchedule] in timeSlot:
                        print('Filtering Results...')
                        os.system('cls')
                        countv2 = countv2  + 1          


        
        if count == len(slotDate) and countv2 == len(timeSlot) and genderFilter == workout['gymArea']:
            break
    if count == len(slotDate) and countv2 == len(timeSlot) and genderFilter == workout['gymArea']:
        WorkoutId = str(workout['identifier'])
        WorkoutDate = workout['dayOfWeek']
        WorkoutSlot = workout['startDateObj'] +  ' to ' + workout['endDateObj']
        print('Successfully Located Timeslot!')
        time.sleep(2)
        print('Day : ' + workout['dayOfWeek'] + ' | Time slot : ' + workout['startDateObj'] +  ' to ' + workout['endDateObj'] + ' | ' + workout['gymArea'])
        print('Total Capacity : ' + str(workout['maxOccupancy']) + ' | Current Capacity : ' + str(workout['currentOccupancy']) + ' | Available Slots : ' + str(workout['availableSlots']) + '\n')
        break

r = s.post('https://www.goodlifefitness.com/content/experience-fragments/goodlife/header/master/jcr:content/root/responsivegrid/header.Update_Last_Login.json')
ping = r
print(r.text)

print('Extracting Credentials...')
print('Regenerating Captcha...')
site_url ='http://2captcha.com/in.php?key=[YOUR 2CAP TOKEN HERE]&method=userrecaptcha&googlekey=6Lfz3I8aAAAAACbq6gVz0yzf9__GZcUmqqdp8WHt&json=1&pageurl=https://www.goodlifefitness.com/book-workout.html'

user_Date = str(datetime.date(datetime.now()))
s = requests.Session()
captcha = s.post(site_url)
captcha = json.loads(captcha.text)


captcha_id = captcha['request']
site_urlv2 = 'http://2captcha.com/res.php?key=[YOUR 2CAP TOKEN HERE]&json=1&action=get&id=' + str(captcha_id)


captcha = s.get(site_urlv2)
response = json.loads(captcha.text)



count = 0
start = time.time()
while response['request'] == 'CAPCHA_NOT_READY':
    r = s.post('https://www.goodlifefitness.com/content/experience-fragments/goodlife/header/master/jcr:content/root/responsivegrid/header.Update_Last_Login.json')
    ping = r
    print(r.text)
    count = count + 1

    captcha = s.get(site_urlv2)
    response = json.loads(captcha.text)
    if count % 5 == 0:
        print('Awaiting Captcha Solver... [' + str(count//5) + ']')
end = time.time()


captcha_webhook = 'INSERT YOUR OWN DISCORD WEBHOOK FOR FUNTIONALITY' 
captcha_stats = {
            'username':'Goodlife Captcha Solves'
        }
captcha_stats['embeds'] = [
    {
        'title':'Captcha V2',
        'fields':[{
            'name':'Time Taken to Solve',
            'value':str(end - start)
        }]

}]

captcha_webhook = requests.post(captcha_webhook, json=captcha_stats)

print('Captcha Tokens Found!'+ '| Time Taken to Solve : ' + str(end - start))    
captcha_token = response['request']
r = s.post('https://www.goodlifefitness.com/content/experience-fragments/goodlife/header/master/jcr:content/root/responsivegrid/header.Update_Last_Login.json')
ping = r
print(r.text)
bookingInfo = {'clubId':clubId, 'timeSlotId':WorkoutId, 'captchaToken':captcha_token}
time.sleep(0.5)
print('Generating Credentials...')
os.system('cls')
logo()
print('\n')
task_num = 0
while True:
    r = s.post('https://www.goodlifefitness.com/content/experience-fragments/goodlife/header/master/jcr:content/root/responsivegrid/header.Update_Last_Login.json')
    ping = r
    print(r.text)
    task_num = task_num + 1
    print('Submitting Info... [' + str(task_num) + ']')
    startv2 = time.time()
    r = s.post('https://www.goodlifefitness.com/content/goodlife/en/book-workout/jcr:content/root/responsivegrid/workoutbooking.CreateWorkoutBooking.json', data=bookingInfo)
    response = (r.text)
    response = json.loads(response)
    print(response)
    print(r.text)
    try:
        test = response['map']['response']['result']
    except KeyError:
        test = response['map']['response']['message']

    if 'TOO_EARLY' or 'PERSON_BUSY' in test:
        print('Error Submitting... [' + str(task_num) + ']\n')
    
    elif test == 'BookedInWaitlist':
        waitListPosition = response['map']['response']['waitListPosition']
        print('Reservation Failure... Waitlist Position : ' + str(waitListPosition))
        failure_webhook = 'INSERT YOUR OWN DISCORD WEBHOOK FOR FUNTIONALITY'
        data = {
            'username':'Goodlife Reservations'
        }
        data['embeds'] = [
            {
                'title':'Reservation Failed',

                'fields':[{
                    'name': 'Location',
                    'value': clubName
                },
                {
                    'name': 'Date',
                    'value':WorkoutDate
                },
                {
                    'name':'Time Slot',
                    'value':WorkoutSlot
                }]
            }
                ]
        webhook = requests.post(failure_webhook, json=data)

    else:
        endv2 = time.time()
        print('Successful Reservation! Time taken to Submit.... ' + str(endv2 - startv2))
        failure_webhook = 'INSERT YOUR OWN DISCORD WEBHOOK FOR FUNTIONALITY'
        data = {
            'username':'Goodlife Reservations'
        }
        data['embeds'] = [
            {
                'title':'Reservation Success',

                'fields':[{
                    'name': 'Location',
                    'value': clubName
                },
                {
                    'name': 'Date',
                    'value':WorkoutDate
                },
                {
                    'name':'Time Slot',
                    'value':WorkoutSlot
                }]
            }
                ]
        webhook = requests.post(failure_webhook, json=data)
        break


r.close()


'''
DIFFERENT RESPONSES THAT CAN BE USEFUL TO DETERMINE SUCCESS OR NOT
{'map': {'response': {'result': 'BookedInWaitlist', 'waitListPosition': 9, 'resultReason': 'ClubFull', 'bookingId': 631317}, 'message': 'API Success Response', 'statusCode': 200}}
API Success Response



{'map': {'response': {'message': '{"errorCode":"PERSON_BUSY","errorDescription":"Unable to book because member is already booked into an appointment at this time."}', 'statusCode': 400}, 'message': 'API Failure Response', 'statusCode': 400}}
API Failure Response

{'map': {'response': {'message': '{"errorCode":"TOO_EARLY","errorDescription":"Unable to book because you must wait until closer to the start time to book."}', 'statusCode': 400}, 'message': 'API Failure Response', 'statusCode': 400}}
API Failure Response 

{'map': {'response': {'message': '{"errorCode":"TOO_EARLY","errorDescription":"Unable to book because you must wait until closer to the start time to book."}', 'statusCode': 400}, 'message': 'API Failure Response', 'statusCode': 400}}
{'message': '{"errorCode":"TOO_EARLY","errorDescription":"Unable to book because you must wait until closer to the start time to book."}', 'statusCode': 400}

{'map': {'response': {'result': 'BookedInWaitlist', 'waitListPosition': 12, 'resultReason': 'ClubFull', 'bookingId': 627360}, 'message': 'API Success Response', 'statusCode': 200}}
{'result': 'BookedInWaitlist', 'waitListPosition': 12, 'resultReason': 'ClubFull', 'bookingId': 627360}
'''

