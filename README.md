# Plenitudo MCP Server Template

A production-ready template for building MCP (Model Context Protocol) servers with:

- **API key auth** — free/pro tiers with monthly quotas
- **x402 micropayments** — USDC on Base, pay-per-call
- **Stripe webhooks** — automatic tier upgrades/downgrades
- **Railway-ready** — single process, configurable data dir

## Quick start

```bash
# Clone and install
git clone https://github.com/knportal/plenitudo-mcp-template.git my-mcp-server
cd my-mcp-server
pip install -r requirements.txt

# Configure
cp .env.example .env
# Edit .env with your Stripe keys and wallet address

# Create an API key
python manage_keys.py create --tier free

# Run
python server.py
```

## Adding your own tools

Edit `server.py` — replace the `hello` tool with your own. Each tool should accept `api_key` and `payment_proof` parameters and use the auth pattern shown in the example.

## Deploy to Railway

1. Push to GitHub
2. Connect the repo in Railway
3. Set environment variables in the Railway dashboard
4. Deploy

## Key management

```bash
python manage_keys.py create --tier free
python manage_keys.py create --tier pro --customer cus_abc123
python manage_keys.py list
python manage_keys.py usage <api_key>
python manage_keys.py deactivate <api_key>
```

## License

MIT
