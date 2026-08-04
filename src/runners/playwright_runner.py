import subprocess

def run_playwright_test(test_file):

    result = subprocess.run(
        [
            "pytest",
            test_file,
            "-v"
        ],
        capture_output=True,
        text=True,
    )

    return {
        "status": "PASSED" if result.returncode == 0 else "FAILED",
        "output": result.stdout
    }