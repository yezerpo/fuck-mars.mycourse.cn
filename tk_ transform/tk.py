import pandas as pd
import json
import os
import base64

local = os.path.dirname(os.path.abspath(__file__))
xlsx_path = os.path.join(local, "tk.xlsx")
tk_path = os.path.join(local, "tk.json")


if __name__ == "__main__":
    df = pd.read_excel(xlsx_path, sheet_name="2025年题库组稿（350+300+350版）")
    selected_data = df[["题目", "答案"]].copy()
    selected_data['答案'] = selected_data['答案'].str.replace('Y', 'A').str.replace('N', 'B')
    selected_data["答案"] = selected_data["答案"].str.replace("|", "", regex=False)
    answer_dict = dict(zip(selected_data["题目"], selected_data["答案"]))
    with open(tk_path, "w", encoding="utf-8") as f:
        json.dump(answer_dict, f, ensure_ascii=False)