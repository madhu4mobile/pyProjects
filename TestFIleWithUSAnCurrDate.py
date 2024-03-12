import random
import string
import os
from datetime import datetime, timedelta


# Function to generate random alphanumeric string
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


# Function to generate random date within a month from today
def generate_random_date():
    today = datetime.now()
    start_date = today - timedelta(days=7)
    random_date = random.choice([start_date + timedelta(days=i) for i in range((today - start_date).days)])
    return random_date.strftime("%m/%d/%Y")


# Function to generate random time in HHMM format
def generate_random_time():
    return datetime.now().strftime("%H%M")


# Function to generate random city name
def generate_random_city():
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego",
              "Dallas", "San Jose"]
    return random.choice(cities)


# Function to generate random state name
def generate_random_state():
    states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
              "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
              "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
              "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina",
              "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
              "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
              "Wisconsin", "Wyoming"]
    return random.choice(states)


# Function to generate random record for PMTHDR
def generate_pmthdr():
    courier_code = generate_random_string(10)
    form_code = generate_random_string(10)
    payment_date = generate_random_date()
    payment_amount = round(random.uniform(10, 1000), 2)
    account_number = random.randint(100000000, 999999999)
    check_number = random.randint(1000, 9999)
    return f"PMTHDR,{courier_code},{form_code},{payment_date},{payment_amount},{account_number},{check_number},"


# Function to generate random record for PAYENM
def generate_payenm():
    payee_name_1 = generate_random_string(20)
    payee_name_2 = generate_random_string(20)
    vendor_number = generate_random_string(8)
    return f"PAYENM,{payee_name_1},{payee_name_2},{vendor_number},"


# Function to generate random record for PYEADD
def generate_pyeadd():
    payee_address_line_1 = generate_random_string(20)
    payee_address_line_2 = generate_random_string(20)
    phone = ''.join(random.choices(string.digits, k=10))
    return f"PYEADD,{payee_address_line_1},{payee_address_line_2},{phone},"


# Function to generate random record for ADDPYE
def generate_addpye():
    payee_address_line_3 = generate_random_string(20)
    payee_address_line_4 = generate_random_string(20)
    return f"ADDPYE,{payee_address_line_3},{payee_address_line_4},"


# Function to generate random record for PYEPOS
def generate_pyepos():
    payee_city = generate_random_city()
    payee_state = generate_random_state()
    payee_zip = ''.join(random.choices(string.digits, k=5))
    payee_country = "USA"
    return f"PYEPOS,{payee_city},{payee_state},{payee_zip},{payee_country},"


# Function to generate random record for RMTDTL
def generate_rmtdtl():
    invoice_number = generate_random_string(10)
    description = generate_random_string(20)
    invoice_date = generate_random_date()
    net_amount = round(random.uniform(10, 1000), 2)
    gross_amount = round(net_amount + random.uniform(0.5, 20), 2)
    discount_amount = round(random.uniform(0, 10), 2)
    return f"RMTDTL,{invoice_number},{description},{invoice_date},{net_amount},{gross_amount},{discount_amount},"


# Main function to generate random data and save it to a text file
def main():
    num_records = int(input("Enter the total number of records (default is 4): ") or "4")
    record_types = [generate_pmthdr, generate_payenm, generate_pyeadd, generate_addpye, generate_pyepos,
                    generate_rmtdtl]

    output_directory = "resources/output/"
    os.makedirs(output_directory, exist_ok=True)
    output_file = os.path.join(output_directory, "output.txt")

    # Use a temporary buffer to count the number of lines
    temp_buffer = []

    with open(output_file, "w") as file:
        temp_buffer.append(
            f"FILHDR,PWS,CDSCHECKS6,{datetime.now().strftime('%m/%d/%Y')},{datetime.now().strftime('%H%M')},\n")

        for _ in range(num_records):
            for record_type in record_types:
                record = record_type()
                temp_buffer.append(record + "\n")

        temp_buffer.append(f"FILTRL,{len(temp_buffer) + 1},\n") # Add 1 to include the FILTRL line itself

        # Write all buffered lines to the file
        file.writelines(temp_buffer)

    print(f"Output file has been saved to: {output_file}")


if __name__ == "__main__":
    main()
