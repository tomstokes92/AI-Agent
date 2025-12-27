from functions.get_files_content import get_file_content
from config import MAX_CHARS

def test_lorem_truncation():
    content = get_file_content("calculator", "lorem.txt")
    assert len(content) > MAX_CHARS
    assert f'truncated at {MAX_CHARS} characters' in content
    print("Lorem truncation test passed")

def run_manual_tests():
    print("\n--- main.py ---")
    print(get_file_content("calculator", "main.py"))

    print("\n--- pkg/calculator.py ---")
    print(get_file_content("calculator", "pkg/calculator.py"))

    print("\n--- /bin/cat (should error) ---")
    print(get_file_content("calculator", "/bin/cat"))

    print("\n--- pkg/does_not_exist.py (should error) ---")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    test_lorem_truncation()
    run_manual_tests()
