# Architecture and development plan

## Current milestone: repository foundation

The first milestone is documentation and basic diagnostics. It is not a VPN implementation.

## Intended components

1. **Client configuration** — use WireGuard's established format and tools; do not implement cryptography ourselves.
2. **Server endpoint** — must be a host that accepts public UDP traffic and permits VPN use.
3. **IP verification** — compare the public egress IP before and after connecting to the tunnel.
4. **Rotation policy** — select among multiple legitimate exit endpoints, or use a host with a documented address-rotation feature. A reconnect to one endpoint alone does not guarantee a new public IP.
5. **Secret handling** — private keys and full client configs stay out of Git. Use local secret storage or CI secrets only when needed.

## Free-hosting constraints

- Render Web Services forward public traffic to one HTTP port. That model is not a general public UDP listener for WireGuard.
- Render Free services can sleep while idle and may restart. They are useful for a web dashboard or development API, not a dependable always-on VPN endpoint.
- GitHub Actions is for automated build and test jobs, not a permanent VPN server.

## Validation checklist

- [ ] Confirm a host explicitly supports WireGuard UDP traffic.
- [ ] Generate keys with WireGuard's own tools on the client and server.
- [ ] Keep private keys out of repository files, logs, screenshots, and issue reports.
- [ ] Confirm the tunnel handshake succeeds.
- [ ] Confirm public IP and DNS behavior while connected.
- [ ] Test what happens when the endpoint is unavailable.
- [ ] Document any free-tier limits and whether the egress IP is static or can change.

## No false claims

A successful build, deployment, health check, or IP-check request is not proof that a VPN tunnel works. The project must report each status separately.
