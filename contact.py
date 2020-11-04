class Contact:
    """
    Class that generates new instances of contacts.
    """

    contact_list = [] # Empty contact list
    
    # Init method up here
    def save_contact(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        Contact.contact_list.append(self)

    def __init__(self,first_name,last_name,number,email):

      # docstring removed for simplicity

        self.first_name = first_name #instance varriable
        self.last_name = last_name
        self.phone_number = number
        self.email = email