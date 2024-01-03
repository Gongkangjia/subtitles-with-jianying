import pysrt
import json
from pathlib import Path

subs = pysrt.open("text.srt")

"""
Windows 上，剪映字幕的工作目录是：USER_HOME + '\AppData\Local\JianyingPro\User Data\Projects\com.lveditor.draft';
macOS 上，剪映字幕的工作目录是：USER_HOME + '/Movies/JianyingPro/User Data/Projects/com.lveditor.draft/'
"""
draft = json.loads(Path("draft_info.json").read_text())

start = 0
for v in draft["materials"]["videos"]:
    slice_a = start
    slice_b = start+v["duration"]
    r_subs = subs.slice(starts_after={"milliseconds":slice_a//1000}, ends_before={"milliseconds":slice_b//1000})
    r_subs.shift(milliseconds=-slice_a//1000)
    r_subs.save(Path(v["path"]).with_suffix(".srt"))
    print(v["path"])
    start += v["duration"]
