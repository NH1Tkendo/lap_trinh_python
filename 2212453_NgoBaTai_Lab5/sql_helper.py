import pyodbc

connectionString = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=.;DATABASE=QLMonAn;UID=sa;PWD=1;Encrypt=no"


def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn


def close_connection(conn):
    if conn:
        conn.close()


def get_nhom_food():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """select TenNhom from NhomMonAn"""
        cursor.execute(select_query)
        records = [record[0] for record in cursor.fetchall()]

        close_connection(connection)
        return records
    except (Exception, pyodbc.Error) as error:
        print("Lỗi: ", error)

def get_tt_food():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """select MaMonAn, TenMonAn, DonViTinh, DonGia, TenNhom from NhomMonAn, MonAn
        where MonAn.Nhom = NhomMonAn.MaNhom"""
        cursor.execute(select_query)
        records = cursor.fetchall()
        close_connection(connection)
        return records
    except (Exception, pyodbc.Error) as error:
        print("Lỗi: ", error)


def cbb_choice(choice):
    try:
        connection = get_connection()  # Hàm kết nối CSDL
        cursor = connection.cursor()

        # Gọi stored procedure
        cursor.execute("{CALL ComboBoxSelection (?)}", choice)

        records = cursor.fetchall()

        close_connection(connection)
        return records
    except (Exception, pyodbc.Error) as error:
        print("Lỗi: ", error)
