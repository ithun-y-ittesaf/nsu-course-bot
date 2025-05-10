import json
import os

DATA_FILE = "data/subscriptions.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_course_for_user(user_id, course, section):
    data = load_data()
    user_courses = data.get(user_id, [])
    if not any(c['course'] == course and c['section'] == section for c in user_courses):
        user_courses.append({'course': course, 'section': section, 'seats': None})
    data[user_id] = user_courses
    save_data(data)

def remove_course_for_user(user_id, course, section):
    data = load_data()
    if user_id not in data:
        return False
    before = len(data[user_id])
    data[user_id] = [c for c in data[user_id] if not (c['course'] == course and c['section'] == section)]
    after = len(data[user_id])
    save_data(data)
    return before != after

def get_all_courses():
    return load_data()

def get_user_courses(user_id):
    return load_data().get(user_id, [])
