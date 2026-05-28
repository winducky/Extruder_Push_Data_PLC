import subprocess
import sys
from pathlib import Path


def convert_all_ui_to_py():
    """
    Tự động tìm tất cả file .ui
    và convert sang .py cùng tên
    """

    current_dir = Path.cwd()

    ui_files = list(current_dir.glob("*.ui"))

    if not ui_files:
        print("Không tìm thấy file .ui")
        return

    for ui_file in ui_files:
        py_file = ui_file.with_suffix(".py")

        try:
            subprocess.run(
                [
                    "pyuic5",
                    "-x",
                    str(ui_file),
                    "-o",
                    str(py_file)
                ],
                check=True,
                capture_output=True,
                text=True
            )

            print(f"[OK] {ui_file.name} -> {py_file.name}")

        except subprocess.CalledProcessError as e:
            print(f"[ERROR] {ui_file.name}")
            print(e.stderr)

        except FileNotFoundError:
            print("Không tìm thấy pyuic5")
            print("Cài bằng: pip install pyqt5")
            sys.exit(1)


if __name__ == "__main__":
    convert_all_ui_to_py()