# invikost

Autonomous Cloud Efficiency & Savings Assurance.

## Version
2.0.0 — Environment Autopilot

## Architecture
- Next.js / TypeScript frontend
- FastAPI / Python backend
- PostgreSQL
- Redis / RQ
- AWS cross-account integration
- Modular monolith with background workers

## First-release scope
- AWS-only
- Non-production EC2 environments
- Read-only discovery and simulation
- Customer-approved EC2 stop/start automation
- Dependency and safety validation
- Health and recovery verification
- Financial savings ledger

## Safety
Production resources are excluded by default.
No automatic resource deletion or termination.
AWS write permissions are enabled only after explicit customer authorization.

## Development
See docs/architecture for technical specifications.