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
from student import Student
from account import Account
LibraryDatabase.loadBooks()


class TestStudent:
    
    account, userType = Account.load_account('student123')

    ## Add test cases for all methods in Student class

    @pytest.mark.parametrize("f_name, l_name, department, account", [
        ("John", "Doe", "Computer Science", account),
        ("Jane", "Adekanbi", "Computer Science", account),
        ("Dansteve", "Ola", "Computer Science", account),])
    def test_student(self, f_name, l_name, department, account):
        newStudent = Student(f_name, l_name, department, account)
        assert newStudent.f_name == f_name
        assert newStudent.l_name == l_name
        assert newStudent.department == department
        assert newStudent.account == account



# %%
