
from phonenumbers import geocoder, carrier
import phonenumbers
import pytz
from datetime import datetime
from timezonefinder import TimezoneFinder

def getinformation(phone_number):

    parsed_number = phonenumbers.parse(phone_number)
    country = geocoder.description_for_number(parsed_number, "en")
    service_provider = carrier.name_for_number(parsed_number, "en")

    region = phonenumbers.region_code_for_number(parsed_number)

    timezone_finder = TimezoneFinder()

    time_zone_str = timezone_finder.timezone_at(lng=0, lat=0)

    result = {}

    if phonenumbers.is_valid_number(parsed_number):
        international_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        national_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
    else:
        print("\n Error: Invalid phone number (inactive number / wrong format).")
            
    

    if time_zone_str:
        time_zone = pytz.timezone(time_zone_str)
        current_time = datetime.now(time_zone)
        
        result["Phone Number"] = phone_number
        result["International Format"] = international_format
        result["National Format"] = national_format
        result["Service Provider"] = service_provider
        result["Country"] = country
        result["Geographical Region"] = region
        result["Time Zone"] = time_zone
        result["Current Time"] = current_time.strftime('%Y-%m-%d %H:%M:%S %Z')

    else:

        result["Phone Number"] = phone_number
        result["International Format"] = international_format
        result["National Format"] = national_format
        result["Service Provider"] = service_provider
        result["Country"] = country
        result["Geographical Region"] = region
        result["Time Zone"] = "Unknow"
        result["Current Time"] = "Unknow"

    return result
