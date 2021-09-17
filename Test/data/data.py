from pathlib import Path


class Whatsapp(object):
    file_for_availability = Path(__file__).parent.parent / 'data/number.xlsx'
    sheet_for_availability = 'Sheet1'
    country_code_BD = '+880'


class Data(object):
    whatsapp_app_package = 'com.whatsapp'
    whatsapp_app_activity = 'com.whatsapp.HomeActivity'
    whatsapp_app_activity_main = 'com.whatsapp.Main'
    whatsapp_app_activity_reg = 'com.whatsapp.registration.EULA'
    # Timeout
    point_five = 0.5
    one_second = 1
    two_seconds = 2
    three_seconds = 3
    four_seconds = 4
    five_seconds = 5
    six_seconds = 6
    seven_seconds = 7
    eight_seconds = 8
    nine_seconds = 9
    ten_seconds = 10
    fifteen_seconds = 15
    twenty_seconds = 20
    twenty_five_seconds = 25
    thirty_seconds = 30
    thirty_five_seconds = 35
    forty_seconds = 40
    forty_five_seconds = 45
    one_minute = 60
    two_minutes = 120
    three_minutes = 180
    four_minutes = 2400
    five_minutes = 3000
