with open('pyproject.toml', 'r') as f:
    content = f.read()

# Add pydantic-settings after pydantic
content = content.replace(
    '"pydantic>=2.11.5",',
    '"pydantic>=2.11.5",\n    "pydantic-settings>=2.8.1",'
)

with open('pyproject.toml', 'w') as f:
    f.write(content)

print("Fixed pyproject.toml")
