import requests
import datetime
import pprint
import time

main_server_api = "https://cdn-api.co-vin.in/api"
states =  "/v2/admin/location/states"
districts_id = "/v2/admin/location/districts"
findbypin = "/v2/appointment/sessions/public/findByPin"
findbydistrict = "/v2​/appointment​/sessions​/public​/findByDistrict"
calendarbypin = "/v2/appointment/sessions/public/calendarByPin"
calendarbydistrict = "/v2/appointment/sessions/public/calendarByDistrict"

headers_api = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

today_date = datetime.datetime.now().strftime("%d-%m-%Y")

# Enter Your Pin address and district_id_pin sbpur(852127,71) 
my_pin = 852127
my_district = 71

# code for finding state,state_id and their respective districts and districts_id
# state_response = requests.get(f'{main_server_api}{states}',headers = headers_api)
# # print(state_response)
# all_dict = {}
# if str(state_response) == '<Response [200]>':
# 	state_response_json = state_response.json()
# 	for state in state_response_json['states']:
# 		all_dict[state['state_name']] = {}
# 		all_dict[state['state_name']]['state_id'] = state['state_id']
# 		all_dict[state['state_name']]['DistrictsWithId'] = {}
# 		district_response = requests.get(f"{main_server_api}{districts_id}/{state['state_id']}", headers = headers_api)
# 		if str(district_response) == '<Response [200]>':
# 			district_response_json = district_response.json()
# 			for dist in district_response_json['districts']:
# 				all_dict[state['state_name']]['DistrictsWithId'][dist['district_name']] = dist['district_id']
# pprint.pprint(all_dict)

print('##################### SEARCHING IN YOUR PIN ADDRESS FOR TODAY ###############################\n')
findbypin_response = requests.get(f'{main_server_api}{findbypin}',params={'pincode':my_pin,'date':today_date}, headers=headers_api)
if str(findbypin_response) == '<Response [200]>':
	findbypin_response_json = findbypin_response.json()
	if len(findbypin_response_json['sessions']) > 0:
		for sessn in findbypin_response_json['sessions']:
			print(f"Date : {sessn['date']}")
			print(f"vaccine is: {sessn['vaccine']} and total vaccine available : {sessn['available_capacity']}")
			print(f"fees for vaccine is: {sessn['fee']}")
			print(f"minimum age required is: {sessn['min_age_limit']}")
			print(f"it is available from {sessn['from']} to {sessn['to']} in the time slot : {sessn['slots']}")
			print(f"the center_name is: {sessn['name']}, center_id is : {sessn['center_id']}, center_address is : {sessn['address']},")
			print(f"Block_name : {sessn['block_name']}, Pincode : {sessn['pincode']}, District_name :{sessn['district_name']}, State : {sessn['state_name']}")
			print("\n\n")
			time.sleep(1.5)

	else:
		print("NO Sessions/slots are available for today")

# print('##################### SEARCHING IN YOUR DISTRICT FOR TODAY ###############################\n')
# findbydistrict_response = requests.get(f'{main_server_api}{findbydistrict}',params={'district_id':my_district,'date':today_date}, headers=headers_api)
# print(findbydistrict_response)
# print(findbydistrict_response.json())
# print("\n\n")


print('##################### SEARCHING IN YOUR PIN ADDRESS FOR NEXT SEVEN DAYS ###############################\n')
calendarbypin_response = requests.get(f'{main_server_api}{calendarbypin}',params={'pincode':my_pin,'date':today_date}, headers=headers_api)
if str(findbypin_response) == '<Response [200]>':
	calendarbypin_response_json = calendarbypin_response.json()
	if len(calendarbypin_response_json['centers']) > 0:
		for cent in calendarbypin_response_json['centers']:
			for sessn in cent['sessions']:
				print(f"Date : {sessn['date']}")
				print(f"vaccine is: {sessn['vaccine']} and total vaccine available are : {sessn['available_capacity']}")
				print(f"fees for vaccine is: {cent['fee_type']}")
				print(f"minimum age required is: {sessn['min_age_limit']}")
				print(f"it is available from {cent['from']} to {cent['to']} in the time slot : {sessn['slots']}")
				print(f"the center_name is: {cent['name']}, center_id is : {cent['center_id']}, center_address is : {cent['address']},")
				print(f"Block_name : {cent['block_name']}, Pincode : {cent['pincode']}, District_name :{cent['district_name']}, State : {cent['state_name']}")
				print("\n\n")
				time.sleep(1.5)

	else:
		print("NO Sessions/slots are available for today")

print('##################### SEARCHING IN YOUR DISRICT FOR NEXT SEVEN DAYS ###############################\n')
calendarbydistrict_response = requests.get(f'{main_server_api}{calendarbydistrict}',params={'district_id':my_district,'date':today_date}, headers=headers_api)

if str(calendarbydistrict_response) == '<Response [200]>':
	calendarbydistrict_response_json = calendarbydistrict_response.json()
	if len(calendarbydistrict_response_json['centers']) > 0:
		for cent in calendarbydistrict_response_json['centers']:
			for sessn in cent['sessions']:
				print(f"Date : {sessn['date']}")
				print(f"vaccine is: {sessn['vaccine']} and total vaccine available are : {sessn['available_capacity']}")
				print(f"fees for vaccine is: {cent['fee_type']}")
				print(f"minimum age required is: {sessn['min_age_limit']}")
				print(f"it is available from {cent['from']} to {cent['to']} in the time slot : {sessn['slots']}")
				print(f"the center_name is: {cent['name']}, center_id is : {cent['center_id']}, center_address is : {cent['address']},")
				print(f"Block_name : {cent['block_name']}, Pincode : {cent['pincode']}, District_name :{cent['district_name']}, State : {cent['state_name']}")
				print("\n\n")
				time.sleep(1.5)

	else:
		print("NO Sessions/slots are available for today")




# print(findbypin_response.json())