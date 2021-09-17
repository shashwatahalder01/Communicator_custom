from utils.excel_utils import *
from data.data import *

file = Path(__file__).parent.parent / 'data/number.xlsx'

sheet = 'Sheet1'


def read_person_message(file, sheet):
    maxRow = getRowCount(file, sheet)
    phone = remove_items(readsinglecol(file, sheet, 2, maxRow, 1), None)
    message = remove_items(readsinglecol(file, sheet, 2, maxRow, 2), None)
    return phone, message
