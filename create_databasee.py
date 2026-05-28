# Tạo database sqlite
import sqlite3

# Tạo kết nối
conn = sqlite3.connect('extruder.sqlite')

# Tạo cursor
cursor = conn.cursor()

# Tạo bảng spec
cursor.execute('''
CREATE TABLE IF NOT EXISTS spec (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ext_code TEXT UNIQUE,
    tire_name TEXT,
    upper_screw_speed real,
    lower_screw_speed real,
    roller_speed_1st real,
    roll_tuc_speed real,
    length real,
    height real,
    weight real,
    conveyor_roller real,
    conveyor_slope real,
    roller_conveyor_belt real,
    cooling_conveyor_belt real,
    tuc_roller real,
    update_by TEXT,           
    update_time TEXT DEFAULT CURRENT_TIMESTAMP
)
''')

# Tạo bảng operator
cursor.execute('''
CREATE TABLE IF NOT EXISTS operator (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    operator_code TEXT UNIQUE,
    operator_name TEXT
)
''')

# Tao bảng plan
cursor.execute('''
CREATE TABLE IF NOT EXISTS plan (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ext_code TEXT UNIQUE,
    sort_order INTEGER DEFAULT 0
)
''')

# Tạo bảng history
cursor.execute('''
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ext_code TEXT,
    operator_code TEXT,
    action TEXT,
    timestamp TEXT DEFAULT CURRENT_TIMESTAMP
)
''')

# Commit thay đổi
conn.commit()

# Đóng kết nối
conn.close()