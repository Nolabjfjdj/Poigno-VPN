# Poigno-VPN

Poigno-VPN is a learning project to build a personal VPN setup with an emphasis on privacy, transparent configuration, and careful testing.

## Important status

This repository is at the initial development stage. It does **not** currently provide a working VPN tunnel, a VPN server, or automatic public-IP rotation.

The first goal is to build and validate the project tooling. A real tunnel will require a supported host that can accept WireGuard UDP traffic. Render Free Web Services are designed for public HTTP services and do not expose a general public UDP port, so they are not a suitable WireGuard endpoint. See the [Render Web Services documentation](https://render.com/docs/web-services).

## Project principles

- Use established VPN technology such as WireGuard rather than inventing cryptography.
- Never commit private keys, client configuration files, or credentials.
- Keep the setup free to develop and test where possible.
- Be explicit about what is and is not running.
- Treat IP rotation as a separate feature: reconnecting to the same VPN endpoint does not inherently change its public exit IP.

## Development

The initial tools are small diagnostics that can be run locally or in a CI workflow. They do not create a VPN tunnel.

See [the architecture notes](docs/ARCHITECTURE.md) for the current plan and hosting constraints.
