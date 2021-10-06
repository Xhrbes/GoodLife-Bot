# GoodLife-Bot
A GoodLife bot that automatically reserves workout sessions using requests.

THIS IS AN OUTDATED VERSION OF THE BOT THAT USED TO WORK ON THE GOODLIFE SITE. THIS IS TO BE USED AS LEARNING MATERIAL AND TO POSSIBLY AID IN CREATING A USABLE BOT ON THE WEBSITE.

The GoodLife reservation system works as follows (As of writing).

#1. A login page protected by a V2 Captcha that is only accesible with valid GoodLife accounts that have a current gym membership.

#2. The club ID & workout timeslot ID will be required for the post request to reserve the appointment (These can be easily scraped on the page HTML with a bit of digging).

#3. A final V2 Captcha will be needed as well as the club location ID & the workout timeslot ID in the post request.

STEPS

#1. Generate a valid V2 Captcha token, and once generated make a post request to the GoodLife login endpoint with the solved Captcha token & a GoodLife account with a valid gym membership.

#2. Once logged in make a request to the website to scrape Club IDs & workout timeslot IDs.

#3. Generate another valid V2 Captcha token and make a final post request to the booking endpoint with the valid Captcha token & the club ID and the workout timeslot ID.

#4. Make a final check to the endpoint to validate whether the reservation was successful or not.



CURRENT BOT INPUT:
For date of workout the input must be in yy-mm-did format, eg 2021-03-02, 2022-10-09, and 2020-03-23. Input must be separated by the hyphen “-“

Time slot input:
Input must be made in military time format i.e. 19:30(7:30pm), 13:00(1:00pm), and 17:45(5:45pm). Input must be separated by the colon “:”
Ignore what the bot prompts you to do as it will cause it to crash

TO DO
- Change the input for the date of the workout (faciliate it for users to utilize it in future versions).
- Add support for multiple accounts
- Add Geolocation support to the bot, GoodLife's website will only load clubs within a certain radius of the location of the ping request. Eg a request made to the GoodLife website from Toronto will only load clubs around the GTA area.
