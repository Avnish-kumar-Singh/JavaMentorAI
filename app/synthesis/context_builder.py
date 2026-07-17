"""
Context Builder

Cleans and merges retrieved chunks before sending them to the LLM.
"""


class ContextBuilder:

    def build(self, documents):

        unique_chunks = []
        seen = set()

        for doc in documents:

            text = doc.page_content.strip()

            if not text:
                continue

            if text in seen:
                continue

            seen.add(text)
            unique_chunks.append(text)

        return "\n\n".join(unique_chunks)