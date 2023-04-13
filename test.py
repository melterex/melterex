import shutil
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(file).resolve().parent
a = int(input())
shutil.rmtree(BASE_DIR)