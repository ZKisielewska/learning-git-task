from faker import Faker

# create BaseContact class with requaired arguments: first_name, last_name, phone and email
class BaseContact:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def contact(self):
        """method displaying a text "Dial 'phone' and call 'first_name and last_name_name'"""
        print(f"Dial {self.phone} and call {self.first_name} {self.last_name}")

    @property
    def label_length(self):
        """method returning the lenght of full name"""
        return len(f"{self.first_name} {self.last_name}")

# create BusinessContact class that inherits from BaseContact class
# additional arguments: position, company, business_phone
class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, phone, email, position, company, business_phone):
        super().__init__(first_name, last_name, phone, email)
        self.position = position
        self.company = company
        self.business_phone = business_phone

    def contact(self):
        """method displaying a text "Dial 'phone' and call 'first_name and last_name_name'"""
        print(f"Dial {self.business_phone} and call {self.first_name} {self.last_name}")

def create_contacts(contact_type, num_contacts):
    """create random labels with two type of parameters: contact_type and num_contact (numbers of labels)"""
    fake = Faker()
    contacts = []
    for _ in range(num_contacts):
        first_name = fake.first_name()
        last_name = fake.last_name()
        phone = fake.phone_number()
        email = fake.email()
        if contact_type == "base":
            contact = BaseContact(first_name, last_name, phone, email)
        elif contact_type == "business":
            position = fake.job()
            company = fake.company()
            business_phone = fake.phone_number()
            contact = BusinessContact(first_name, last_name, phone, email, position, company, business_phone)
        else:
            raise ValueError("Invalid contact type. Must be 'base' or 'business'.")
        contacts.append(contact)
    return contacts

# Create base contacts
base_contacts = create_contacts("base", 5)

# Create business contacts
business_contacts = create_contacts("business", 5)

# Display base contacts
print("Base Contacts:")
for contact in base_contacts:
    contact.contact()
    print(f"Label Length: {contact.label_length}")
    print()

# Display business contacts
print("Business Contacts:")
for contact in business_contacts:
    contact.contact()
    print(f"Label Length: {contact.label_length}")
    print()