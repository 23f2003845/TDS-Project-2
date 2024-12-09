# /// script
# dependencies = [
#   "requests",
#   "pandas"
# ]
# ///
import os
import requests
import pandas as pd
import sys


# Utility function to talk to llm
def question_llm(question, context=""):
    auth_token = os.environ["AIPROXY_TOKEN"]
    res = requests.post(
        "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a well experienced data scientist and analyst. You have been provided some data and you need to narrate a story from it. Go ahead and make it creative",
                },
                {"role": "user", "content": f"{question}. \n Context: f{context}"},
            ],
        },
    )

    result = res.json()

    print(result)
    return result["choices"][0]["message"]["content"] if not result["error"] else None


# Utility function to open file.
def open_file(file_path):
    df = pd.read_csv(file_path)
    return df


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Filename required")
        sys.exit()

    filenames = sys.argv[1:]
    question_llm("Are you ready?")
