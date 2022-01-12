"""Script to load data quotation on database.
"""
from quotation.utils.last_quotation import last_quotation

if __name__ == '__main__':
    last_quotation(days=10)
