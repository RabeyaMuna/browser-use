# Fix anthropic/chat.py - the dict splat approach doesn't work with overloads
with open('browser_use/llm/anthropic/chat.py', 'r') as f:
    content = f.read()

# Replace both create() call patterns to use explicit kwargs

# First call pattern (non-structured output)
old1 = """\t\t\t\tcreate_kwargs = dict(model=self.model, messages=anthropic_messages)
\t\t\t\tif system_prompt is not None:
\t\t\t\t\tcreate_kwargs['system'] = system_prompt
\t\t\t\tcreate_kwargs.update(self._get_client_params_for_invoke())
\t\t\t\tresponse = await self.get_client().messages.create(**create_kwargs)"""

new1 = """\t\t\t\tinvoke_params = self._get_client_params_for_invoke()
\t\t\t\tif system_prompt is not None:
\t\t\t\t\tresponse = await self.get_client().messages.create(
\t\t\t\t\t\tmodel=self.model,
\t\t\t\t\t\tmessages=anthropic_messages,
\t\t\t\t\t\tsystem=system_prompt,
\t\t\t\t\t\t**invoke_params,
\t\t\t\t\t)
\t\t\t\telse:
\t\t\t\t\tresponse = await self.get_client().messages.create(
\t\t\t\t\t\tmodel=self.model,
\t\t\t\t\t\tmessages=anthropic_messages,
\t\t\t\t\t\t**invoke_params,
\t\t\t\t\t)"""

content = content.replace(old1, new1)

# Second call pattern (structured output with tools)
old2 = """\t\t\t\t\tcreate_kwargs = dict(model=self.model, messages=anthropic_messages, tools=[tool])
\t\t\t\t\tif system_prompt is not None:
\t\t\t\t\t\tcreate_kwargs['system'] = system_prompt
\t\t\t\t\tcreate_kwargs['tool_choice'] = tool_choice
\t\t\t\t\tcreate_kwargs.update(self._get_client_params_for_invoke())
\t\t\t\t\tresponse = await self.get_client().messages.create(**create_kwargs)"""

new2 = """\t\t\t\t\tinvoke_params = self._get_client_params_for_invoke()
\t\t\t\t\tif system_prompt is not None:
\t\t\t\t\t\tresponse = await self.get_client().messages.create(
\t\t\t\t\t\t\tmodel=self.model,
\t\t\t\t\t\t\tmessages=anthropic_messages,
\t\t\t\t\t\t\ttools=[tool],
\t\t\t\t\t\t\tsystem=system_prompt,
\t\t\t\t\t\t\ttool_choice=tool_choice,
\t\t\t\t\t\t\t**invoke_params,
\t\t\t\t\t\t)
\t\t\t\t\telse:
\t\t\t\t\t\tresponse = await self.get_client().messages.create(
\t\t\t\t\t\t\tmodel=self.model,
\t\t\t\t\t\t\tmessages=anthropic_messages,
\t\t\t\t\t\t\ttools=[tool],
\t\t\t\t\t\t\ttool_choice=tool_choice,
\t\t\t\t\t\t\t**invoke_params,
\t\t\t\t\t\t)"""

content = content.replace(old2, new2)

with open('browser_use/llm/anthropic/chat.py', 'w') as f:
    f.write(content)

print("Fixed anthropic/chat.py (v2)")

# Fix aws/chat_anthropic.py - same pattern
with open('browser_use/llm/aws/chat_anthropic.py', 'r') as f:
    content = f.read()

# First call pattern
old1 = """\t\t\t\t\tcreate_kwargs = dict(model=self.model, messages=anthropic_messages)
\t\t\t\t\tif system_prompt is not None:
\t\t\t\t\t\tcreate_kwargs['system'] = system_prompt
\t\t\t\t\tcreate_kwargs.update(self._get_client_params_for_invoke())
\t\t\t\t\tresponse = await self.get_client().messages.create(**create_kwargs)"""

new1 = """\t\t\t\t\tinvoke_params = self._get_client_params_for_invoke()
\t\t\t\t\tif system_prompt is not None:
\t\t\t\t\t\tresponse = await self.get_client().messages.create(
\t\t\t\t\t\t\tmodel=self.model,
\t\t\t\t\t\t\tmessages=anthropic_messages,
\t\t\t\t\t\t\tsystem=system_prompt,
\t\t\t\t\t\t\t**invoke_params,
\t\t\t\t\t\t)
\t\t\t\t\telse:
\t\t\t\t\t\tresponse = await self.get_client().messages.create(
\t\t\t\t\t\t\tmodel=self.model,
\t\t\t\t\t\t\tmessages=anthropic_messages,
\t\t\t\t\t\t\t**invoke_params,
\t\t\t\t\t\t)"""

content = content.replace(old1, new1)

# Second call pattern
old2 = """\t\t\t\t\tcreate_kwargs = dict(model=self.model, messages=anthropic_messages, tools=[tool])
\t\t\t\t\tif system_prompt is not None:
\t\t\t\t\t\tcreate_kwargs['system'] = system_prompt
\t\t\t\t\tcreate_kwargs['tool_choice'] = tool_choice
\t\t\t\t\tcreate_kwargs.update(self._get_client_params_for_invoke())
\t\t\t\t\tresponse = await self.get_client().messages.create(**create_kwargs)"""

new2 = """\t\t\t\t\tinvoke_params = self._get_client_params_for_invoke()
\t\t\t\t\tif system_prompt is not None:
\t\t\t\t\t\tresponse = await self.get_client().messages.create(
\t\t\t\t\t\t\tmodel=self.model,
\t\t\t\t\t\t\tmessages=anthropic_messages,
\t\t\t\t\t\t\ttools=[tool],
\t\t\t\t\t\t\tsystem=system_prompt,
\t\t\t\t\t\t\ttool_choice=tool_choice,
\t\t\t\t\t\t\t**invoke_params,
\t\t\t\t\t\t)
\t\t\t\t\telse:
\t\t\t\t\t\tresponse = await self.get_client().messages.create(
\t\t\t\t\t\t\tmodel=self.model,
\t\t\t\t\t\t\tmessages=anthropic_messages,
\t\t\t\t\t\t\ttools=[tool],
\t\t\t\t\t\t\ttool_choice=tool_choice,
\t\t\t\t\t\t\t**invoke_params,
\t\t\t\t\t\t)"""

content = content.replace(old2, new2)

with open('browser_use/llm/aws/chat_anthropic.py', 'w') as f:
    f.write(content)

print("Fixed aws/chat_anthropic.py (v2)")

# Fix google/serializer.py - change return type annotation
with open('browser_use/llm/google/serializer.py', 'r') as f:
    content = f.read()

# Change return type from tuple[ContentListUnion, str | None] to tuple[list[Content], str | None]
content = content.replace(
    'def serialize_messages(messages: list[BaseMessage]) -> tuple[ContentListUnion, str | None]:',
    'def serialize_messages(messages: list[BaseMessage]) -> tuple[list[Content], str | None]:'
)

with open('browser_use/llm/google/serializer.py', 'w') as f:
    f.write(content)

print("Fixed google/serializer.py (v2)")
