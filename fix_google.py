with open('browser_use/llm/google/serializer.py', 'r') as f:
    content = f.read()

# Fix: Change ContentListUnion to list[Content]
content = content.replace(
    'formatted_messages: ContentListUnion = []',
    'formatted_messages: list[Content] = []'
)

with open('browser_use/llm/google/serializer.py', 'w') as f:
    f.write(content)

print("Fixed google/serializer.py")
