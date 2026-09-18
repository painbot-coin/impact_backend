# Impact / SalesGPT backend

API for an outbound sales assistant. Users, campaigns, and contacts sit in SQL. Agents run through LangChain/SalesGPT. Twilio handles voice.

## What is in here

- FastAPI routes for auth, campaigns, contacts
- SalesGPT agent, prompts, tools, and stages
- Twilio voice webhook hooks
- JWT sessions

## Stack

Python, FastAPI, LangChain, Twilio, SQL
