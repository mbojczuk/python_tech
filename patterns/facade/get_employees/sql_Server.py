from .abs_facde import AbsFacade
import pyodbc
from . import CONNSTR, QUERY

class GetEmployeesFacade(AbsFacade):
    def get_employees(self):
        connection = pyodbc.connect(CONNSTR)
        cursor = connection.cursor()
        cursor.execute(QUERY)
        for row in cursor:
            print(row.FirstName, row.LastName)
        connection.commit()
        connection.close()