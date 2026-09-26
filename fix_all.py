import re

# ---------- Fix 4: browser_use/llm/anthropic/chat.py ----------
with open('browser_use/llm/anthropic/chat.py', 'r') as f:
    content = f.read()

# Fix the two calls to create() to conditionally pass system
# First call (line 141-146)
old = """\t\t\t\tresponse = await self.get_client().messages.create(
\t\t\t\t\tmodel=self.model,
\t\t\t\t\tmessages=anthropic_messages,
\t\t\t\t\tsystem=system_prompt or NOT_GIVEN,
\t\t\t\t\t**self._get_client_params_for_invoke(),
\t\t\t\t)"""

new = """\t\t\t\tcreate_kwargs = dict(model=self.model, messages=anthropic_messages)
\t\t\t\tif system_prompt is not None:
\t\t\t\t\tcreate_kwargs['system'] = system_prompt
\t\t\t\tcreate_kwargs.update(self._get_client_params_for_invoke())
\t\t\t\tresponse = await self.get_client().messages.create(**create_kwargs)"""

content = content.replace(old, new)

# Second call (line 191-198)
old = """\t\t\t\t\tresponse = await self.get_client().messages.create(
\t\t\t\t\t\tmodel=self.model,
\t\t\t\t\t\tmessages=anthropic_messages,
\t\t\t\t\t\ttools=[tool],
\t\t\t\t\t\tsystem=system_prompt or NOT_GIVEN,
\t\t\t\t\t\ttool_choice=tool_choice,
\t\t\t\t\t\t**self._get_client_params_for_invoke(),
\t\t\t\t\t)"""

new = """\t\t\t\t\tcreate_kwargs = dict(model=self.model, messages=anthropic_messages, tools=[tool])
\t\t\t\t\tif system_prompt is not None:
\t\t\t\t\t\tcreate_kwargs['system'] = system_prompt
\t\t\t\t\tcreate_kwargs['tool_choice'] = tool_choice
\t\t\t\t\tcreate_kwargs.update(self._get_client_params_for_invoke())
\t\t\t\t\tresponse = await self.get_client().messages.create(**create_kwargs)"""

content = content.replace(old, new)

with open('browser_use/llm/anthropic/chat.py', 'w') as f:
    f.write(content)

print("Fixed anthropic/chat.py")

# ---------- Fix 5: browser_use/llm/aws/chat_anthropic.py ----------
with open('browser_use/llm/aws/chat_anthropic.py', 'r') as f:
    content = f.read()

# Fix import - AsyncAnthropicBedrock is not exported from anthropic top-level
content = content.replace(
    'from anthropic import (\n\t\tNOT_GIVEN,\n\t\tAPIConnectionError,\n\t\tAPIStatusError,\n\t\tAsyncAnthropicBedrock,\n\t\tRateLimitError,\n\t)',
    'from anthropic import (\n\t\tNOT_GIVEN,\n\t\tAPIConnectionError,\n\t\tAPIStatusError,\n\t\tRateLimitError,\n\t)\nfrom anthropic.lib.bedrock import AsyncAnthropicBedrock'
)

# Fix the two calls to create() to conditionally pass system
# First call (line 163-168)
old = """\t\t\t\t\tresponse = await self.get_client().messages.create(
\t\t\t\t\t\tmodel=self.model,
\t\t\t\t\t\tmessages=anthropic_messages,
\t\t\t\t\t\tsystem=system_prompt or NOT_GIVEN,
\t\t\t\t\t\t**self._get_client_params_for_invoke(),
\t\t\t\t\t)"""

new = """\t\t\t\t\tcreate_kwargs = dict(model=self.model, messages=anthropic_messages)
\t\t\t\t\tif system_prompt is not None:
\t\t\t\t\t\tcreate_kwargs['system'] = system_prompt
\t\t\t\t\tcreate_kwargs.update(self._get_client_params_for_invoke())
\t\t\t\t\tresponse = await self.get_client().messages.create(**create_kwargs)"""

content = content.replace(old, new)

# Second call (line 205-212)
old = """\t\t\t\t\tresponse = await self.get_client().messages.create(
\t\t\t\t\t\tmodel=self.model,
\t\t\t\t\t\tmessages=anthropic_messages,
\t\t\t\t\t\ttools=[tool],
\t\t\t\t\t\tsystem=system_prompt or NOT_GIVEN,
\t\t\t\t\t\ttool_choice=tool_choice,
\t\t\t\t\t\t**self._get_client_params_for_invoke(),
\t\t\t\t\t)"""

new = """\t\t\t\t\tcreate_kwargs = dict(model=self.model, messages=anthropic_messages, tools=[tool])
\t\t\t\t\tif system_prompt is not None:
\t\t\t\t\t\tcreate_kwargs['system'] = system_prompt
\t\t\t\t\tcreate_kwargs['tool_choice'] = tool_choice
\t\t\t\t\tcreate_kwargs.update(self._get_client_params_for_invoke())
\t\t\t\t\tresponse = await self.get_client().messages.create(**create_kwargs)"""

content = content.replace(old, new)

with open('browser_use/llm/aws/chat_anthropic.py', 'w') as f:
    f.write(content)

print("Fixed aws/chat_anthropic.py")

# ---------- Fix 6: browser_use/llm/deepseek/chat.py ----------
with open('browser_use/llm/deepseek/chat.py', 'r') as f:
    content = f.read()

# Fix the base_url and timeout type issues - use type: ignore
content = content.replace(
    'base_url=self.base_url,',
    'base_url=self.base_url,  # type: ignore[reportArgumentType]'
)

content = content.replace(
    'timeout=self.timeout,',
    'timeout=self.timeout,  # type: ignore[reportArgumentType]'
)

with open('browser_use/llm/deepseek/chat.py', 'w') as f:
    f.write(content)

print("Fixed deepseek/chat.py")

# ---------- Fix 7: browser_use/llm/google/serializer.py ----------
with open('browser_use/llm/google/serializer.py', 'r') as f:
    content = f.read()

# Fix the Content type - need to convert Part to Content properly
# Line 96: formatted_messages.append(final_message)
# final_message is Content(role=role, parts=message_parts)
# The issue is Content is not assignable to ContentListUnion elements
# ContentListUnion is a union of allowed types, and Content may not be in it
# Let's use Part objects instead

# Actually, looking at the error more carefully:
# "Argument of type "Content" cannot be assigned to parameter "object" of type "str | PIL_Image | File | Part" in function "append""
# This means formatted_messages.append(final_message) is trying to add Content to something that expects str | PIL_Image | File | Part
# So formatted_messages is being treated as a list that expects Part-like items, not Content items
# The issue is ContentListUnion type - it might be PartListUnion or something

# Let me check what ContentListUnion actually is
# ContentListUnion = list[Content]  # probably
# But the .append() expects individual items, and if ContentListUnion is list[Content],
# then append should accept Content...

# Actually looking at the error: "parameter "object" of type "str | PIL_Image | File | Part""
# This suggests formatted_messages is a list of Parts, not Contents
# The type annotation says ContentListUnion but it's behaving differently

# Let me check
pass  # We'll investigate more
