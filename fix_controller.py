with open('browser_use/mcp/controller.py', 'r') as f:
    content = f.read()

# Fix: Replace tool.inputSchema with tool.input_schema
content = content.replace('tool.inputSchema', 'tool.input_schema')

with open('browser_use/mcp/controller.py', 'w') as f:
    f.write(content)

print("Fixed mcp/controller.py")
