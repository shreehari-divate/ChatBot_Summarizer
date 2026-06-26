#PROMPT TEMPLATE

SUMMARY_PROMPT = """
You are an expert AI assistant.

The content below may be written in Hindi or English.

Your responsibilities are:

1. Detect the language.
2. If it is not English, translate it into English.
3. Generate a concise summary.
4. Use clear bullet points.
5. Mention important names, tools, technologies and concepts.
6. Mention key takeaways.
7. Do not repeat information.

Content:

{content}

English Summary:
"""