from tkinter import messagebox
import json

def save_to_json(data,fileLink):
    try:
        # Load existing data if the file exists
        try:
            with open(fileLink, 'r', encoding='utf-8') as json_file:
                existing_data = json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []

        # Append new data
        existing_data.append(data)

        # Save back to JSON file
        with open(fileLink, 'w', encoding='utf-8') as json_file:
            json.dump(existing_data, json_file, ensure_ascii=False, indent=4)

        messagebox.showinfo(title='Success', message='Dữ liệu đã được lưu vào diemso.json')
    except Exception as e:
        messagebox.showerror(title='Error', message=f'Không thể lưu dữ liệu: {e}')