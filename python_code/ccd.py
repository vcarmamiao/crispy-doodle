import pandas as pd

# 定义每个表的结构
tables = {
    "Users": [
        ("user_id", "INT AUTO_INCREMENT PRIMARY KEY", "用户的唯一标识"),
        ("name", "VARCHAR(50) NOT NULL", "用户名"),
        ("password", "VARCHAR(255) NOT NULL", "用户密码"),
        ("user_type", "ENUM('resident', 'admin', 'superadmin') NOT NULL", "用户类型"),
        ("email", "VARCHAR(100)", "用户邮箱"),
        ("phone", "VARCHAR(20)", "用户电话"),
        ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP", "创建时间"),
        ("updated_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP", "更新时间")
    ],
    "Buildings": [
        ("building_id", "INT AUTO_INCREMENT PRIMARY KEY", "楼栋的唯一标识"),
        ("name", "VARCHAR(100) NOT NULL", "楼栋名称"),
        ("address", "VARCHAR(255) NOT NULL", "楼栋地址"),
        ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP", "创建时间"),
        ("updated_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP", "更新时间")
    ],
    "Units": [
        ("unit_id", "INT AUTO_INCREMENT PRIMARY KEY", "单元的唯一标识"),
        ("building_id", "INT", "外键，关联 Buildings 表"),
        ("name", "VARCHAR(100) NOT NULL", "单元名称"),
        ("floor", "INT NOT NULL", "楼层"),
        ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP", "创建时间"),
        ("updated_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP", "更新时间")
    ],
    "Houses": [
        ("house_id", "INT AUTO_INCREMENT PRIMARY KEY", "房子的唯一标识"),
        ("current_resident_id", "INT", "外键，关联 Users 表，当前住户"),
        ("owner_id", "INT", "外键，关联 Users 表，户主"),
        ("building_id", "INT", "外键，关联 Buildings 表，几栋"),
        ("unit_id", "INT", "外键，关联 Units 表，几单元"),
        ("house_number", "VARCHAR(50)", "门牌号"),
        ("area", "FLOAT", "面积"),
        ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP", "创建时间"),
        ("updated_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP", "更新时间")
    ],
    "ParkingSpaces": [
        ("parking_space_id", "INT AUTO_INCREMENT PRIMARY KEY", "停车位的唯一标识"),
        ("building_id", "INT", "外键，关联 Buildings 表，几栋"),
        ("parking_number", "VARCHAR(50)", "车位号"),
        ("owner_id", "INT", "外键，关联 Users 表，所有人"),
        ("current_user_id", "INT", "外键，关联 Users 表，现在用户"),
        ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP", "创建时间"),
        ("updated_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP", "更新时间")
    ],
    "Bills": [
        ("bill_id", "INT AUTO_INCREMENT PRIMARY KEY", "账单的唯一标识"),
        ("balance", "DECIMAL(10, 2)", "余额"),
        ("amount_change", "DECIMAL(10, 2)", "变化金额"),
        ("new_balance", "DECIMAL(10, 2)", "变化后余额"),
        ("time", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP", "时间"),
        ("note", "TEXT", "备注")
    ],
    "PropertyFees": [
        ("fee_id", "INT AUTO_INCREMENT PRIMARY KEY", "物业费的唯一标识"),
        ("house_id", "INT", "外键，关联 Houses 表"),
        ("start_date", "DATE", "开始收取时间"),
        ("last_date", "DATE", "上次收取时间"),
        ("amount_due", "DECIMAL(10, 2)", "还需收取金额")
    ],
    "Notifications": [
        ("notification_id", "INT AUTO_INCREMENT PRIMARY KEY", "通知的唯一标识"),
        ("time", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP", "时间"),
        ("notifier_id", "INT", "外键，关联 Users 表，通知人ID"),
        ("content", "TEXT", "内容")
    ],
    "RepairRequests": [
        ("repair_id", "INT AUTO_INCREMENT PRIMARY KEY", "维修事件的唯一标识"),
        ("initiator_id", "INT", "外键，关联 Users 表，维修发起人"),
        ("priority", "ENUM('low', 'medium', 'high')", "优先级"),
        ("location", "VARCHAR(255)", "地点"),
        ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP", "创建时间"),
        ("updated_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP", "更新时间")
    ],
    "Leases": [
        ("lease_id", "INT AUTO_INCREMENT PRIMARY KEY", "租赁事件的唯一标识"),
        ("tenant_id", "INT", "外键，关联 Users 表，租户ID"),
        ("owner_id", "INT", "外键，关联 Users 表，所属人ID"),
        ("start_date", "DATE", "开始时间"),
        ("end_date", "DATE", "结束时间")
    ],
    "Owners": [
        ("owner_id", "INT PRIMARY KEY", "业主的唯一标识，关联 Users 表"),
        ("house_ids", "TEXT", "拥有的房产IDs（JSON格式）"),
        ("parking_space_ids", "TEXT", "拥有的停车位IDs（JSON格式）"),
        ("email", "VARCHAR(100)", "邮箱"),
        ("phone", "VARCHAR(20)", "电话")
    ]
}

# 创建一个 DataFrame 来存储表结构
table_data = []
for table_name, columns in tables.items():
    for column in columns:
        table_data.append((table_name, column[0], column[1], column[2]))

df = pd.DataFrame(table_data, columns=["Table Name", "Column Name", "Data Type", "Description"])

# 将数据保存到 CSV 文件
csv_file_path = "community_property_management_system_tables.csv"
df.to_csv(csv_file_path, index=False)

print(f"CSV 文件已生成并保存在 {csv_file_path}")