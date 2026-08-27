import json
import os

#file data json thi dung luon thu vien
def parse_dataset(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    jobs = data["jobs"]
    resources = data["resources"]
    operations = data["operations"]
    print(f"--- {os.path.basename(file_path)} ---") #in test
    print(f"Tổng số Jobs: {len(jobs)} -> {jobs}")
    print(f"Tổng số Resources (máy): {len(resources)} -> {resources}")
    print(f"Tổng số Operations: {len(operations)}")
    return data #tra ve du lieu

def get_details(data):
    operations = data["operations"]
    op_jobs = data["operations_jobs"]
    op_types = data["operations_operation_types"]
    op_classes = data["operation_classes"]
    parse_ops = {}
    for op in operations:
        job = op_jobs[op]
        op_type = op_types[op]
        is_assembly = op_classes.get(op, 1)
        parse_ops[op] = { #nhet vao trong parse_ops duoi dang json
            "job": job,
            "type": op_type,
            "is_assembly": is_assembly,
            "class_name": "Assembly" if is_assembly == 1 else "Component" #toan tu 3 ngoi
        }
    return parse_ops



file_test = os.path.join("sm", "sm_0_1.json")
data = parse_dataset(file_test)
results = get_details(data)
