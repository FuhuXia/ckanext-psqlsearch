#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

cleanup() {
  docker compose -f docker-compose.test.yml down --volumes --remove-orphans
}

trap cleanup EXIT

docker compose -f docker-compose.test.yml run --rm test
