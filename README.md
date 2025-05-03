# A sample implement to use fastmcp

## Prerequisite
- use uv to setup your dev enviroment

## Dev/Test run
```
$ fastmcp dev server.py
```

## Production run
```
$ ./src/server.py
```

## Connect Ollama model & MCP server
```
# install mcphost command
$ go install github.com/mark3labs/mcphost@latest

# install python dependencies
$ uv pip install -r requirements.txt

# start ollama service
$ sudo service ollama start

# add absolute path to the server.py into sample-mcp-config.json
$ nano sample-mcp-config.json

# start mcphost
$ mcphost -m ollama:qwen2.5:latest --config <path to ./sample-mcp-config>
```
