with open('browser_use/dom/playground/test_accessibility.py', 'r') as f:
    content = f.read()

# Fix: Add type: ignore for page.accessibility
content = content.replace(
    'ax_tree_interesting = await page.accessibility.snapshot(interesting_only=True)',
    'ax_tree_interesting = await page.accessibility.snapshot(interesting_only=True)  # type: ignore[reportAttributeAccessIssue]'
)

with open('browser_use/dom/playground/test_accessibility.py', 'w') as f:
    f.write(content)

print("Fixed test_accessibility.py")
