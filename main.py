#!/usr/bin/env python3
import argparse
from src.client import chat, stream_chat, load_prompt


def main():
    parser = argparse.ArgumentParser(description="Claude API client")
    parser.add_argument("message", help="Message to send to Claude")
    parser.add_argument(
        "--prompt",
        default="assistant",
        help="Name of the system prompt file in prompts/ (default: assistant)",
    )
    parser.add_argument(
        "--stream",
        action="store_true",
        help="Stream the response token by token",
    )
    args = parser.parse_args()

    system_prompt = load_prompt(args.prompt)

    if args.stream:
        stream_chat(args.message, system_prompt=system_prompt)
    else:
        response = chat(args.message, system_prompt=system_prompt)
        print(response)


if __name__ == "__main__":
    main()
