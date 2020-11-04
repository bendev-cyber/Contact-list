import unittest #importing the unittest module
from contact import Contact #importing the contact class

class TestContact(unittest.TestCase): #inherits from unittest.testcase
    def setUp(self): #setup method allows us to defne instructions that will be executed before each method test
        
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = Contact("John","doe","0712345678","john@ms.com") # create contact object


    def test_init(self): #test instance

        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.first_name,"John") #assertEqual is a testCase method ued to find unexpected results
        self.assertEqual(self.new_contact.last_name,"doe")
        self.assertEqual(self.new_contact.phone_number,"0712345678")
        self.assertEqual(self.new_contact.email,"john@ms.com")


    def test_save_contact(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''

        self.new_contact.save_contact() # saving the new contact
        self.assertEqual(len(Contact.contact_list),1)

        # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Contact.contact_list = []

        
    def test_save_multiple_contact(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_contact.save_contact()
            test_contact = Contact("Test","user","0712345678","test@user.com") # new contact
            test_contact.save_contact()
            self.assertEqual(len(Contact.contact_list),2)

           
   
if __name__ == '__main__':
    unittest.main()