import subprocess
import sys
from pathlib import Path


def build_exe():

    current_dir = Path.cwd()

    main_file = current_dir / "GiaoDien.py"
    version_file = current_dir / "version.txt"
    icon_file = current_dir / "icon.ico"
    app_name = "Extruder_App"
    if not main_file.exists():
        print("Không tìm thấy GiaoDien.py")
        sys.exit(1)

    if not version_file.exists():
        print("Không tìm thấy version.txt")
        sys.exit(1)

    if not icon_file.exists():
        print("Không tìm thấy icon.ico")
        sys.exit(1)

    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",

        "--noconfirm",
        "--clean",

        "--onefile",

        "--noupx",

        "--windowed",

        "--icon",
        str(icon_file),

        "--version-file",
        str(version_file),

        "--name",
        str(app_name),

        str(main_file)
    ]

    try:

        print("Đang build EXE...\n")

        subprocess.run(
            cmd,
            check=True
        )

        print("\nBuild thành công")
        print(f"EXE: dist/{app_name}.exe")

    except subprocess.CalledProcessError:
        print("\nBuild thất bại")
        sys.exit(1)


if __name__ == "__main__":
    build_exe()