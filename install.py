import os

os.system(
    "pyinstaller --distpath cloudTalk/cloudTalk --workpath cloudTalk/build --clean --specpath cloudTalk -i=logo.ico -n 云上畅谈 -w -F cloudTalk.py"
)
