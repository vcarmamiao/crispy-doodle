from graphviz import Digraph

# 创建一个有向图
dot = Digraph(comment='ER Diagram for Community Property Management System')

# 定义节点和属性
nodes = {
    "Users": ["user_id", "name", "password", "user_type", "email", "phone", "created_at", "updated_at"],
    "Houses": ["house_id", "current_resident_id", "owner_id", "building_id", "unit_id", "house_number", "area", "created_at", "updated_at"],
    "ParkingSpaces": ["parking_space_id", "building_id", "parking_number", "owner_id", "current_user_id", "created_at", "updated_at"],
    "Bills": ["bill_id", "balance", "change", "new_balance", "time", "note"],
    "PropertyFees": ["fee_id", "house_id", "start_date", "last_date", "amount_due"],
    "Notifications": ["notification_id", "time", "notifier_id", "content"],
    "RepairRequests": ["repair_id", "initiator_id", "priority", "location", "created_at", "updated_at"],
    "Leases": ["lease_id", "tenant_id", "owner_id", "start_date", "end_date"],
    "Owners": ["owner_id", "house_ids", "parking_space_ids", "email", "phone"],
    "Buildings": ["building_id", "name", "address", "created_at", "updated_at"],
    "Units": ["unit_id", "building_id", "name", "floor", "created_at", "updated_at"]
}

# 添加节点和属性
for node, attributes in nodes.items():
    dot.node(node, node)
    for attr in attributes:
        dot.node(f'{node}_{attr}', attr, shape='ellipse')
        dot.edge(node, f'{node}_{attr}')

# 添加关系
relations = [
    ("Houses", "Users", "current_resident_id"),
    ("Houses", "Users", "owner_id"),
    ("ParkingSpaces", "Users", "owner_id"),
    ("ParkingSpaces", "Users", "current_user_id"),
    ("Bills", "PropertyFees", "fee_id"),
    ("RepairRequests", "Users", "initiator_id"),
    ("Leases", "Users", "tenant_id"),
    ("Leases", "Users", "owner_id"),
    ("Owners", "Users", "owner_id"),
    ("Houses", "Units", "unit_id"),
    ("Units", "Buildings", "building_id")
]

for rel in relations:
    dot.node(f'{rel[0]}_{rel[1]}', rel[2], shape='diamond')
    dot.edge(rel[0], f'{rel[0]}_{rel[1]}')
    dot.edge(f'{rel[0]}_{rel[1]}', rel[1])

# 保存和渲染图像
dot.render('community_property_management_system_er_diagram', format='png', cleanup=True)