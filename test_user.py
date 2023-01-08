###
# Name: Dansteve Adekanbi
# Student ID: 22178806
# Course Title: CMP7244 Software Development
# Course Code: CMP7244
###

#%%
import pytest
from datetime import timedelta
import datetime
from user import User
from libraryDatabase import LibraryDatabase
from account import Account
LibraryDatabase.loadBooks()


class TestUser:
    pass
    ## Add test cases for all methods in User class

    @pytest.mark.parametrize("f_name, l_name, account", [
        ("John", "Doe", Account("John", "Doe", "student123", "student")),
        ("Jane", "Adekanbi", Account("Jane", "Adekanbi", "student123", "student")),
        ("Dansteve", "Ola", Account("Dansteve", "Ola", "student123", "student")),])
    def test_user(self, f_name, l_name, account):
        newUser = User(f_name, l_name, account)
        assert newUser.f_name == f_name
        assert newUser.l_name == l_name
        assert newUser.account == account

    @pytest.mark.parametrize("word, length", [("John", 4),("Jane Ola", 4), ("Dansteve", 4)])
    def test_ellipsisWord(self, word, length):
        assert User.ellipsisWord(
            word, length) == word[0:length - 3] + "..." if len(word) > length else word

    @pytest.mark.parametrize("date, days", [("01/01/2020 00:00:00", 1), ("01/01/2020 00:00:00", 2), ("01/01/2020 00:00:00", 3)])
    def test_get_date_after(self, date, days):
        assert User.get_date_after(date, days) == (
            datetime.datetime.strptime(date, "%d/%m/%Y %H:%M:%S") + datetime.timedelta(days=days)).strftime("%d/%m/%Y %H:%M:%S")
        

        