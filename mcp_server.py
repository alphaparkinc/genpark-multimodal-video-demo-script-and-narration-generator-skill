"""MCP server for Multimodal Video Demo Script Generator."""
import sys
import json
from client import VideoDemoScriptGenerator

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "generate_demo_script",
                "description": "Generates structured video chapters and narration copy from UI steps",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "workflow_title": {"type": "string"},
                        "steps": {"type": "array"}
                    },
                    "required": ["workflow_title", "steps"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "generate_demo_script":
            args = params.get("arguments", {})
            res = VideoDemoScriptGenerator.generate_demo_script(args.get("workflow_title", ""), args.get("steps", []))
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
