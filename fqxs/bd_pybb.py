"""

time: 2023.9.10
cron:  
new Env('py版本查看');

"""

import sys
print(f"你的Python版本为 {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")