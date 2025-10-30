import pandas as pd
import json
import os

local = os.path.dirname(os.path.abspath(__file__))
tkxlsx = os.path.join(local, "tk.xlsx")
tkjson = os.path.join(local, "tk.json")

def excel_to_answer_json(excel_path, sheet_name, output_json_path):
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    selected_data = df[["题目", "答案"]].copy()
    selected_data['答案'] = selected_data['答案'].str.replace('Y', 'A').str.replace('N', 'B')
    selected_data["答案"] = selected_data["答案"].str.replace("|", "", regex=False)
    answer_dict = dict(zip(selected_data["题目"], selected_data["答案"]))
    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(answer_dict, f, ensure_ascii=False, indent=4)
    return answer_dict

if __name__ == "__main__":
    excel_file = tkxlsx
    sheet_name = "2025年题库组稿（350+300+350版）"
    output_json = tkjson
    result = excel_to_answer_json(excel_file, sheet_name, output_json)