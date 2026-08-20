from analyzer import analyze_log

file_path = input("Enter log file path: ")

result = analyze_log(file_path)

if result is None:
    print("❌ File not found.")
else:
    print("\n📊 LogWatch Report")
    print("=" * 35)
    print(f"Total lines : {result['total']}")
    print(f"Errors      : {result['errors']}")
    print(f"Warnings    : {result['warnings']}")
    print(f"Info        : {result['info']}")
