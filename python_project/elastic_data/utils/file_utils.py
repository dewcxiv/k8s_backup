from datetime import datetime

def generate_dated_excel_filename(base_name="report"):
    date_str = datetime.now().strftime("%Y-%m-%d")
    return f"{base_name}_{date_str}.xlsx"
