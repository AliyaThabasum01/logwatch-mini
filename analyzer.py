def analyze_log(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        return None

    result = {
        "total": len(lines),
        "errors": 0,
        "warnings": 0,
        "info": 0
    }

    for line in lines:
        level = line.upper()

        if "ERROR" in level:
            result["errors"] += 1
        elif "WARNING" in level or "WARN" in level:
            result["warnings"] += 1
        elif "INFO" in level:
            result["info"] += 1

    return result
