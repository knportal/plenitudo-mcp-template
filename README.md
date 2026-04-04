# Plenitudo MCP Server Template

Clone this to launch a new MCP server with x402 micropayments pre-wired.

## Getting Started

1. Clone this repo
2. Edit `server.py` — replace `hello_world` with your tool logic
3. Update the server name in `FastMCP("my-mcp-server", ...)`
4. Push to GitHub → deploy on Railway in 3 steps

## Deploy to Railway

1. **New Project** → Deploy from GitHub repo → select your fork
2. **Add env vars:**
   - `X402_WALLET_ADDRESS` = `0x9053FeDC90c1BCB4a8Cf708DdB426aB02430d6ad`
   - `X402_PRICE_USDC` = `0.001`
   - `DATA_DIR` = `/data`
3. **Add Persistent Volume** at mount path `/data` (keeps your data across deploys)

That's it — Railway auto-deploys on every push to main.

## Payment Flow

Every tool call requires a `payment_proof` (Base transaction hash):

1. No proof → server returns x402 instructions with wallet address + price
2. Caller sends USDC on Base, gets tx hash back
3. Caller re-calls tool with `payment_proof=<tx_hash>`
4. Server verifies on-chain and executes the tool

Revenue lands at: `0x9053FeDC90c1BCB4a8Cf708DdB426aB02430d6ad`

## File Structure

```
server.py       — Your MCP tools (edit this)
x402.py         — Payment verification (don't touch)
config.py       — Config from env vars (don't touch)
requirements.txt
railway.toml    — Railway deployment config
nixpacks.toml   — Build config
.env.example    — Env var reference
```
