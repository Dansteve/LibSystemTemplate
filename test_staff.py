###
# Name: Dansteve Adekanbi
# Student ID: 22178806
# Course Title: CMP7244 Software Development
# Course Code: CMP7244
###

#%%
import pytest
from user import User
from libraryDatabase import LibraryDatabase
from staff import Staff
from account import Account
LibraryDatabase.loadBooks()

class TestStaff:
    account, userType = Account.load_account('staff123')
    liberian = Staff(account.f_name, account.l_name, '', account)

    ## Add test cases for all methods in Staff class

    @pytest.mark.parametrize("f_name, l_name, department, account", [
        ("John", "Doe", "Computer Science", account),
        ("Jane", "Adekanbi", "Computer Science", account),
        ("Dansteve", "Ola", "Computer Science", account),])
    def test_staff(self, f_name, l_name, department, account):
        newStaff = Staff(f_name, l_name, department, account)
        assert newStaff.f_name == f_name
        assert newStaff.l_name == l_name
        assert newStaff.department == department
        assert newStaff.account == account


        
