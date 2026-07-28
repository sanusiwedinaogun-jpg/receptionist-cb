# receptionist-cb
a friendly rule based receptionist chatbot for a Mr Ogun

Submission Overview
1. The Task
The objective of this project was to build a deterministic, rule-based chatbot in Python. The system is designed to run in a continuous interactive loop, process user inputs reliably, map queries to pre-defined intents without using generative LLMs, handle unrecognized inputs gracefully, and provide a clear exit strategy.

2. My Solution
I built a virtual front-desk receptionist for Mr. Ogun’s office. To make the interaction feel natural, the logic engine scans incoming user sentences for target keywords (such as "appointment", "hours", or "location") rather than requiring exact keyword matches. When a user asks a question in plain conversational English, the bot detects the key phrase and returns the appropriate response from its knowledge base.

3. Requirements & Rules Followed
Continuous Input Loop: Enclosed in a while True: cycle to maintain an active session until the user decides to stop.

Input Sanitization: Normalizes all raw inputs using .lower().strip() to strip trailing spaces and ignore uppercase/lowercase variations.

Structured Knowledge Base: Built with a dictionary containing over 10 distinct receptionist intents to keep response logic organized and modular.

Keyword Matching: Iterates through the knowledge base to inspect if a known intent exists within the user's input string.

Fallback Safety Net: Uses a default response mechanism when an input doesn't contain any recognized key phrases, preventing crashes or unexpected errors.

Graceful Termination: Listens for the "exit" command to break the loop cleanly and shut down the session.
