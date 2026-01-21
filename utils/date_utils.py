from datetime import datetime

def convert_ddmmyyyy_to_iso(date_str: str) -> str:
    """
    Converts date from DD/MM/YYYY to YYYY-MM-DD
    """
    return datetime.strptime(date_str, "%d/%m/%Y").strftime("%Y-%m-%d")