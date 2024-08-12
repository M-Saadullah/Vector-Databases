mkdir -p ~/.streamlit/credentials.toml

echo "\
[server]\n\
port = $PORT\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml
