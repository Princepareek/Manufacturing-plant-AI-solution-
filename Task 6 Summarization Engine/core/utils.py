import os
from datetime import datetime

def save_summary(summary_text, output_dir="outputs/summaries"):
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(output_dir, f"summary_{timestamp}.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(summary_text)
    return file_path
