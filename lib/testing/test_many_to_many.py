from many_to_many import Author, Book, Contract
import pytest

def test_book_init():
    """Test Book class initializes with title"""
   

def test_author_init():
    """Test Author class initializes with name"""
   

def test_contract_init():
    """Test Contract class initializes with author, book, date, royalties"""
    
def test_contract_validates_author():
    """Test Contract class validates author of type Author"""
   

    with pytest.raises(Exception):
        Contract("Author", book, date, royalties)

def test_contract_validates_book():
    """Test Contract class validates book of type Book"""
   

    with pytest.raises(Exception):
        Contract(author, "Book", date, royalties)

def test_contract_validates_date():
    """Test Contract class validates date of type str"""
   

    with pytest.raises(Exception):
        Contract(author, book, 1012001, royalties)

def test_contract_validates_royalties():
    """Test Contract class validates royalties of type int"""
    

    with pytest.raises(Exception):
        Contract(author, book, date, "Royalties")

def test_author_has_contracts():
    """Test Author class has method contracts() that returns a list of its contracts"""
    

    

def test_author_has_books():
    """Test Author class has method books() that returns a list of its books"""
    
def test_book_has_contracts():
    """Test Book class has method contracts() that returns a list of its contracts"""
    

def test_book_has_authors():
    """Test Book class has method authors() that returns a list of its authors"""
    

def test_author_can_sign_contract():
    """Test Author class has method sign_contract() that creates a contract for an author and book"""
   

def test_author_has_total_royalties():
    """Test Author class has method total_royalties that gets the sum of all its related contracts' royalties"""
   

    

def test_contract_contracts_by_date():
    """Test Contract class has method contracts_by_date() that sorts all contracts by date"""
    Contract.all = []
   