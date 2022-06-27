# Executes parallel http get with curl against our demo web app
xargs -I % -P 8 curl -I "http://localhost:8887" < <(printf '%s\n' {1..10000})
