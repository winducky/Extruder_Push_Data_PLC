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
    ext_type TEXT,
    mold_number TEXT,
    rubber_upper TEXT,
    rubber_lower TEXT,
    length REAL,
    height REAL,
    weight REAL,
    upper_screw_speed REAL,
    lower_screw_speed REAL,
    roller_speed_1st REAL,
    roll_tuc_speed REAL,
    conveyor_roller REAL,
    conveyor_slope REAL,
    roller_conveyor_belt REAL,
    cooling_conveyor_belt REAL,
    tuc_roller REAL,
    tuc_press_head REAL,
    tuc_conveyor_belts REAL,
    weight_auto REAL,
    rubber_mattress REAL,
    height_mattress REAL,
    thick_mattress REAL,
    weight_mattress REAL,
    weight_with_tuc REAL,
    pcs_spec INTEGER,
    color TEXT,
    engraving TEXT,
    irv_code TEXT,
    spec_number TEXT,
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
    ext_code TEXT,
    sort_order INTEGER DEFAULT 0,
    plan_code TEXT
)
''')

# Tạo bảng history
cursor.execute('''
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ext_code TEXT,
    operator_code TEXT,
    action TEXT,
    plan_code TEXT,
    timestamp TEXT DEFAULT CURRENT_TIMESTAMP
)
''')

# Commit thay đổi
conn.commit()

# Đóng kết nối
conn.close()