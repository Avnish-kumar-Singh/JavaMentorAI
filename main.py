"""
Main Entry Point
"""

import pyperclip
from prompt_toolkit import PromptSession
from prompt_toolkit.formatted_text import HTML

from app.graph.builder import build_graph

session = PromptSession()


def get_user_input() -> str:
    """
    Type a question and press Enter to submit normally.
    To submit pasted/multi-line code reliably, copy it to the
    clipboard first, then type PASTE and press Enter — this reads
    the full clipboard content directly, avoiding terminal paste
    truncation issues.
    """

    print("\n===================================")
    print("JavaMentorAI")
    print("===================================")
    print("Type your question, or type PASTE and press Enter")
    print("to submit Java code copied to your clipboard.")
    print()

    text = session.prompt(HTML("<ansicyan><b>Ask JavaMentorAI:</b></ansicyan> "))

    if text.strip().upper() == "PASTE":
        clipboard_content = pyperclip.paste()
        print(f"[DEBUG] Loaded {len(clipboard_content)} characters from clipboard")
        return clipboard_content.strip()

    return text.strip()


def main():

    graph = build_graph()

    conversation_history = []

    while True:

        user_query = get_user_input()
        print(f"[DEBUG] Captured {len(user_query)} characters, {user_query.count(chr(10))+1} lines")

        if not user_query:
            continue

        if user_query.lower() in ("exit", "quit"):
            break

        state = {
            "messages": conversation_history,
            "user_query": user_query,
            "intent": "",
            "selected_tool": "",
            "context": "",
            "response": "",
            "status": "",
            "error": "",
        }

        result = graph.invoke(state)

        print("\n==============================")
        print("JavaMentorAI")
        print("==============================\n")

        print(result["response"])

        response_content = result["response"]

        if isinstance(response_content, dict):
            response_content = response_content.get("message", str(response_content))
        elif not isinstance(response_content, str):
            response_content = str(response_content)

        conversation_history.append({"role": "user", "content": user_query})
        conversation_history.append({"role": "assistant", "content": response_content})


if __name__ == "__main__":
    main()