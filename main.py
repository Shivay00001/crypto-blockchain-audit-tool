"""Top-level entry point: delegates to the real CLI in src/main.py.

Run: python main.py --bytecode 0x6080...  (or --file path/to/bytecode.txt)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

from main import main  # noqa: E402

if __name__ == "__main__":
    main()
