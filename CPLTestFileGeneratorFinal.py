import random
import string


# Function to generate random alphanumeric string
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


# Function to generate random date in MM/DD/YYYY format
def generate_random_date():
    return f"{random.randint(1, 12):02d}/{random.randint(1, 28):02d}/{random.randint(2000, 2023)}"


# Function to generate random time in HHMM format
def generate_random_time():
    return f"{random.randint(0, 23):02d}{random.randint(0, 59):02d}"


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
    payee_city = generate_random_string(15)
    payee_state = generate_random_string(10)
    payee_zip = ''.join(random.choices(string.digits, k=5))
    payee_country = generate_random_string(10)
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
    num_records = 5  # Number of records to generate
    record_types = [generate_pmthdr, generate_payenm, generate_pyeadd, generate_addpye, generate_pyepos,
                    generate_rmtdtl]

    with open("output.txt", "w") as file:
        file.write(f"FILHDR,PWS,CDSCHECKS6,{generate_random_date()},{generate_random_time()},\n")

        for _ in range(num_records):
            record_type = random.choice(record_types)
            record = record_type()
            file.write(record + "\n")

        file.write(f"FILTRL,{num_records},")


if __name__ == "__main__":
    main()
