---
name: railway
description: >-
  Railway cloud platform deployment, management, debugging, and service scaling workflow.
  Use when deploying Telegram bots, web apps, databases, and monitoring deployments on Railway.
---

# Railway Deployment & Management Skill

This skill provides step-by-step guidance and automation for deploying applications to Railway.

## Core Capabilities
- **Deploying Services**: Creating and configuring services using GitHub repositories or Dockerfiles.
- **Environment Variables**: Setting up production secrets (`BOT_TOKEN`, `API_KEYS`, etc.).
- **Health Checks & Ports**: Ensuring containers bind properly to `$PORT` with lightweight HTTP servers.
- **Troubleshooting & Logs**: Reading build logs, detecting crash causes, and fixing dependency conflicts.

## Best Practices for Telegram Bots on Railway
1. **Always use Dockerfile**: Direct `python:3.12-slim` container avoids Nixpacks/mise buildpack errors.
2. **Health Check Port**: Always bind an aiohttp/FastAPI HTTP server to `PORT` environment variable so Railway knows the container is alive.
3. **Single Polling Instance**: Never run local polling simultaneously with Railway to avoid `TelegramConflictError`.
