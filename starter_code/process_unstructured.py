import re

# ==========================================
# ROLE 2: ETL/ELT BUILDER
# ==========================================


def clean_pdf_text(raw_text: str) -> str:
    # Remove noise like HEADER_PAGE_1 and FOOTER_PAGE_1
    cleaned = re.sub(r'HEADER_PAGE_\d+', '', raw_text)
    cleaned = re.sub(r'FOOTER_PAGE_\d+', '', cleaned)
    return cleaned.strip()
def process_pdf_data(raw_json: dict) -> dict:
    content = raw_json.get("extractedText", "")
    content = clean_pdf_text(content)
    return {
        "document_id": raw_json.get("docId"),
        "source_type": "pdf",
        "author": raw_json.get("author"),
        "category": raw_json.get("category"),
        "content": content,
        "timestamp": raw_json.get("timestamp"),
    }

def process_video_data(raw_json: dict) -> dict:
    # TODO: Map dữ liệu thô từ Video sang định dạng chuẩn (giống PDF)
    # Lưu ý các key của Video: video_id, creator_name, transcript, category, published_timestamp
     return {
        "document_id": raw_json.get("video_id"),
        "source_type": "video",
        "author": raw_json.get("creator_name"),
        "category": raw_json.get("category"),
        "content": raw_json.get("transcript"),
        "timestamp": raw_json.get("published_timestamp"),
    }

