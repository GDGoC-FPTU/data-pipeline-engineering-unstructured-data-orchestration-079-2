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
    content = raw_json.get("extractedText", "") or ""
    content = clean_pdf_text(content)
    return {
        "document_id": raw_json.get("docId"),
        "source_type": "PDF",
        "author": raw_json.get("author") or "",
        "category": raw_json.get("docCategory") or raw_json.get("category") or "",
        "content": content,
        "timestamp": raw_json.get("createdAt") or raw_json.get("timestamp") or "",
    }

def process_video_data(raw_json: dict) -> dict:
    transcript = raw_json.get("transcript", "") or ""
    transcript = transcript.strip()

    return {
        "document_id": raw_json.get("video_id"),
        "source_type": "Video",
        "author": raw_json.get("creator_name") or "",
        "category": raw_json.get("category") or "",
        "content": transcript,
        "timestamp": raw_json.get("published_timestamp") or "",
    }

