$ComposeFile = "$PSScriptRoot/../compose/docker-compose.infrastructure.yml"
$EnvFile = "$PSScriptRoot/../../.env"

docker compose `
    --env-file $EnvFile `
    -f $ComposeFile `
    up -d