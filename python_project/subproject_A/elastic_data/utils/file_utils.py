from datetime import datetime

def generate_dated_excel_filename(prefix: str, output_dir: str):
    from datetime import datetime
    date_str = datetime.now().strftime("%Y%m%d")
    filename = f"{prefix}_{date_str}.xlsx"
    return f"{output_dir}/{filename}"

