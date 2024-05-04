import re

truckmodels = ['model 2518', 'model 9016', 'model tipper', 'model dost', 'model partner']

truckparts = {'model 2518': [
                            {'part-no': 'F8835100', 'name': 'fuel filter', 'price': 3569 },
                            {'part-no': 'F7A01500', 'name': 'oil filter', 'price': 4371 },
                            {'part-no': 'F7B01100 ', 'name': 'AIR FILTER OUTER', 'price': 6934 },
                            {'part-no': 'F7B01200', 'name': 'AIR FILTER INNER', 'price': 1759 },
                            {'part-no': 'B1304301', 'name': 'CLUTCH PLATE', 'price': 15929 },
                            {'part-no': 'B1391801 ', 'name': 'PRESSURE PLATE', 'price': 22248 }
                            ],
                'model 9016': [
                            {'part-no': 'F8835100', 'name': 'fuel filter', 'price': 2569 },
                            {'part-no': 'X4001000', 'name': 'oil filter', 'price': 737 },
                            {'part-no': 'X8806400', 'name': 'AIR FILTER OUTER', 'price': 1241 },
                            {'part-no': 'X8806500', 'name': 'AIR FILTER INNER', 'price': 5861 },
                            {'part-no': 'B1301407', 'name': 'CLUTCH PLATE', 'price': 21707 },
                            {'part-no': 'B1301401', 'name': 'PRESSURE PLATE', 'price': 36816 }
                            ],
                'model partner': [
                            {'part-no': '164032VB1A', 'name': 'fuel filter', 'price': 3856 },
                            {'part-no': '152092VB0A', 'name': 'oil filter', 'price': 1179 },
                            {'part-no': '165462VE0A', 'name': 'AIR FILTER OUTER', 'price': 7145 },
                            {'part-no': '302102VE0A', 'name': 'CLUTCH PLATE', 'price': 9376 },
                            {'part-no': 'B1301401', 'name': 'PRESSURE PLATE', 'price': 9453 }
                            ],
                'model dost': [
                            {'part-no': 'F7A00180', 'name': 'fuel filter', 'price': 661 },
                            {'part-no': '1F7A00170', 'name': 'oil filter', 'price': 2242 },
                            {'part-no': '165462VA1A ', 'name': 'AIR FILTER OUTER', 'price': 1793 },
                            {'part-no': '301002VA1A', 'name': 'CLUTCH PLATE', 'price': 4313 },
                            {'part-no': '302102VA1A', 'name': 'PRESSURE PLATE', 'price': 3683 }
                            ],            
             }

class Trucks:

    truckentries = {}

    def __init__(self, driver, phone, company, owner, owner_email, model, reg, chasis, engine_no, mileage):
        self.driver = driver
        self.phone = phone
        self.company = company
        self.owner = owner
        self.owner_email = owner_email
        self.model = model
        self.reg = reg
        self.chasis = chasis
        self.engine_no = engine_no
        self.mileage = mileage

    def truckSignup(self):
        registration_no = self.reg
        truckentries[registration_no] = self.__init__

print('')
print('STEP 1: SECURITY GUARD TRUCK ENTRY')
print('')

validate_driver = False
while validate_driver == False:
    try:
        drivers_name = str(raw_input("Please enter driver's name and press enter: "))
        if drivers_name.isalpha() == False:
            raise TypeError
        else:
            validate_driver = True
    except TypeError:
        print("ERROR: please supply a valid alphabetical name only")
    
validate_phone = True
while validate_phone:
    try:
        phone_no = raw_input("Please enter driver's phone number and press enter: ")
        phone_no = int(phone_no)
        if phone_no:
            validate_phone = False
    except ValueError:
        print('ERROR: please supply numerical values only')

        

company_name = raw_input("Please enter company name and press enter: ")

validate_owner = False
while validate_owner == False:
    try:
        owners_name = raw_input("Please enter owner's name and press enter: ")
        if owners_name.isalpha() == False:
            raise TypeError
        else:
            validate_owner = True
    except TypeError:
        print("ERROR: please supply a valid alphabetical owners name only")
        

email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
validate_email = False


while validate_email == False:
    owner_emailaddress = raw_input("Please enter owner's email address and press enter: ")
    valid_email = re.match(email_regex, owner_emailaddress)
    if valid_email:
        validate_email = True
    else:
        print('Enter a valid email address')

validate_model = False
while validate_model == False:
    input_truck_model = raw_input("Please enter the truck model and press enter: ")
    truck_model = input_truck_model.lower()
    if truck_model.lower() not in truckmodels:
        print('ERROR: The truck model not in our list of trucks we repair Re-enter or press ctrl c to quit')
    else:
        validate_model = True

truck_registration = raw_input("Please enter truck registration number and press enter: ")
chasis_number = raw_input("Please enter chasis number and press enter: ")
engine_number = raw_input("Please enter engine number and press enter: ")

validate_mileage = False

while validate_mileage == False:
    try:
        car_mileage = int(raw_input("Please enter car mileage in km and press enter: "))
        if car_mileage:
            validate_mileage = True
    except ValueError:
        print('PLEASE ENTER NUMERICAL VALUES ONLY')
        


new_truck = Trucks(drivers_name,phone_no,company_name,owners_name,owner_emailaddress,truck_model,
                    truck_registration,chasis_number,engine_number,car_mileage)

print('')
print('STEP 2: ASSESS AND SELECT THE PARTS THAT NEED REPAIR')
print('INSTRUCTIONS: Type YES if part needs repair and NO if doesn\'t require repair')
print('')

total_cost = 0
quantity = 0
repair_parts = [] 

if new_truck.model == 'model tipper':
    print('spare parts not listed in table for repair')

else:
    for i in truckparts[new_truck.model]:
        repair_part = raw_input('Enter YES or NO if ' + i['name'] + ' is to be repaired: ')
        if repair_part.upper() == 'YES':
            quantity += 1
            total_cost += (i['price'] * 1.16)
            repair_parts.append(i['name'])


print('')
print('STEP : MAILING  TO ' + new_truck.owner_email + ' IN PROGRESS.............')
print('')
print('quantity: ' + str(quantity))
print('parts to be repaired: ') 
 
for i in repair_parts:
    print('     - ' + i)

print('Total cost: ' +  str(total_cost))
print('')