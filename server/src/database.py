import pymysql.cursors
import os

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", 3306)
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_DATABASE = os.getenv("DB_DATABASE", "intros-ai")

database = pymysql.connect(
     host=DB_HOST,
     port=DB_PORT,
     user=DB_USER,
     password=DB_PASSWORD,
     db=DB_DATABASE
)

def insert(table, columns, values):
     """Insert rows into a given table

     Args:
         table (String): The table to add the rows to
         columns (List of Strings): The column names
         values (List of Strings): The values

     Returns:
         Int: The number of rows affected by the insert statement
     """
     cursorObject = database.cursor()
     insert_statement = "INSERT INTO {} ({}) VALUES ('{}')".format(table, ", ".join(columns), ", ".join(values))
     affected_rows = cursorObject.execute(insert_statement)
     database.commit()
     return affected_rows

# columns can either take the list of columns to select or an empty list or None to select all columns
def select(table, columns=None):
     """Select rows from a given table

     Args:
         table (String): The table to select from
         columns (List of Strings, optional): The columns to add to the result of selected rows. Defaults to None.

     Returns:
         List of dicts: List of key/value dicts for rows returned with the column names
     """
     rows_list = []
     if not columns:
          columns_str = "*"
     else:
          columns_str = ", ".join(columns)
     cursorObject = database.cursor()
     insertStatement = "SELECT {} FROM {}".format(columns_str, table)
     cursorObject.execute(insertStatement)
     rows = cursorObject.fetchall()
     num_fields = len(cursorObject.description)
     field_names = [i[0] for i in cursorObject.description]
     for row in rows:
          record = {}
          for i in range(num_fields):
               record[field_names[i]] = row[i]
          rows_list.append(record)
     return rows_list

def delete(table, id):
     """Delete one row from a table provided its ID

     Args:
         table (String): The table to delete from
         id (Int): The ID of the row to delete

     Returns:
         Int: The affected rows by the delete statement, 1 if a row was deleted and 0 if not
     """
     cursorObject = database.cursor()
     delete_statement = "DELETE FROM {} WHERE id={}".format(table, id)
     affected_rows = cursorObject.execute(delete_statement)
     database.commit()
     return affected_rows

def update_bool(table, id, column):
     """Update a boolean column to its opposite in a table provided for a row provided its ID

     Args:
         table (String): The table to update
         id (Int): The ID of the row to update
         column (String): The column to update

     Returns:
         Int: The affected rows by the update statement, 1 if a row was updated and 0 if not
     """
     cursorObject = database.cursor()
     update_statement = "UPDATE {} SET {} = NOT {} WHERE id = {}".format(table, column, column, id)
     affected_rows = cursorObject.execute(update_statement)
     database.commit()
     return affected_rows
