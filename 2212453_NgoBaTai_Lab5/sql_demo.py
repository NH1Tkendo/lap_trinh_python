import pyodbc

print(pyodbc.drivers())

connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=.;DATABASE=QLSinhVien;UID=sa;PWD=1;Encrypt=no'

def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn

def close_connection(conn):
    if conn:
        conn.close()

def get_all_class():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """select * from Lop"""
        cursor.execute(select_query)
        records = cursor.fetchall()

        print("Danh sách các lớp là: ")
        for row in records:
            print('*'*50)
            print("Mã lớp: ", row[0])
            print("Tên lớp: ", row[1])

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Lỗi: ", error)


def get_all_SinhVien():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """select * from SinhVien, Lop where SinhVien.MaLop = Lop.ID"""
        cursor.execute(select_query)
        records = cursor.fetchall()

        print("Danh sách tất cả sinh viên:")
        print(f"{'Mã số'.ljust(10)} {'Họ tên'.ljust(25)} {'Mã lớp'.ljust(10)} {'Tên lớp'.ljust(10)}")
        print("-" * 50)

        for row in records:
            print(f"{str(row[0]).ljust(10)} {str(row[1]).ljust(25)} {str(row[2]).ljust(10)} {str(row[4]).ljust(10)}")

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Lỗi: ", error)


def get_class_by_id(class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """select * from Lop where id = ?"""

        params = (class_id,)
        cursor.execute(select_query, params)
        record = cursor.fetchone()

        print(f"Thông tin lớp có id = {class_id} là: ")
        print("Mã lớp: ", record[0])
        print("Tên lớp: ", record[1])

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Lỗi: ", error)


def get_student_by_id(sinhvien_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """select * from SinhVien where id = ?"""

        params = (sinhvien_id,)
        cursor.execute(select_query, params)
        record = cursor.fetchone()

        print(f"Thông tin lớp có id = {sinhvien_id} là: ")
        print("Mã số: ", record[0])
        print("Họ tên: ", record[1])
        print("Mã lớp: ", record[2])

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Lỗi: ", error)


def get_student_by_classid(class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """select * from SinhVien where MaLop = ?"""
        params = (class_id,)
        cursor.execute(select_query, params)
        record = cursor.fetchall()

        print(f"Thông tin lớp co ma lop la {class_id} là: ")
        for a in record:
            print("Mã số: ", a[0])
            print("Họ tên: ", a[1])

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Lỗi: ", error)

def find_student(class_id, name):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = f"""select * from SinhVien where HoTen LIKE '%{name}%' and MaLop = {class_id}"""
        cursor.execute(select_query)
        record = cursor.fetchall()

        print(f"Thông tin lớp co ma lop la {class_id} là: ")
        for a in record:
            print("Mã số: ", a[0])
            print("Họ tên: ", a[1])

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Lỗi: ", error)


def insert_class(class_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """INSERT INTO Lop(TenLop) VALUES (?)"""
        cursor.execute(select_query, (class_name,))
        connection.commit()
        print("Them thanh cong")

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Lỗi: ", error)


def insert_sinhvien(name, class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """INSERT INTO SinhVien(HoTen, MaLop) VALUES (?,?)"""
        cursor.execute(select_query, (name,class_id))
        connection.commit()
        print("Them thanh cong")

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Lỗi: ", error)


insert_sinhvien("wwdad",3)
