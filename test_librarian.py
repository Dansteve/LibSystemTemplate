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
from librarian import Liberian
from account import Account
LibraryDatabase.loadBooks()


class TestLiberian:

    account, userType = Account.load_account('librarian123')
    liberian = Liberian(account.f_name, account.l_name, '', account)

    ## Add test cases for all methods in Liberian class

    @pytest.mark.parametrize("f_name, l_name, department, account", [
        ("John", "Doe", "Computer Science", account),
        ("Jane", "Adekanbi", "Computer Science", account),
        ("Dansteve", "Ola", "Computer Science", account),])
    def test_liberian(self, f_name, l_name, department, account):
        newLiberian = Liberian(f_name, l_name, department, account)
        assert newLiberian.f_name == f_name
        assert newLiberian.l_name == l_name
        assert newLiberian.department == department
        assert newLiberian.account == account
