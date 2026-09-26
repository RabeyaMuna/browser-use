import re

with open('browser_use/browser/storage_state_watchdog.py', 'r') as f:
    content = f.read()

# Fix 1: Add cast import at the top 
content = content.replace(
    'from typing import Any, ClassVar',
    'from typing import Any, ClassVar, cast'
)

# Fix 2: Fix the _last_cookie_state assignment
content = content.replace(
    "self._last_cookie_state = storage_state.get('cookies', []).copy()",
    "self._last_cookie_state = cast(list[Cookie], storage_state.get('cookies', []).copy())"
)

with open('browser_use/browser/storage_state_watchdog.py', 'w') as f:
    f.write(content)

print("Fixed storage_state_watchdog.py")
