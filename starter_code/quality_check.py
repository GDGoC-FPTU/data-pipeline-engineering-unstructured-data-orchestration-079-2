# ==========================================
# ROLE 3: OBSERVABILITY & QA ENGINEER
# ==========================================

def run_semantic_checks(doc_dict: dict) -> bool:
    content = doc_dict.get("content", "")
    # Check 1: Empty content is a failure
    if not content or len(content.strip()) < 10:
        print(f"Watchman Alert: Empty or insufficient content")
        return False
    # Check 2: Semantic corruption tags
    toxic_keywords = ["hate", "violence", "abuse", "terrorism"]
    for word in toxic_keywords:
        if word.lower() in content.lower():
            print(f"Watchman Alert:")
            return False
    return True
