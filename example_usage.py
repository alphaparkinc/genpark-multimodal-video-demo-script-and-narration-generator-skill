"""Example usage for Multimodal Video Demo Script Generator."""
from client import VideoDemoScriptGenerator

if __name__ == "__main__":
    steps = [
        {"action_name": "API Authentication Setup", "estimated_duration_sec": 6, "narration_detail": "Add environment tokens safely.", "ui_element": "settings-auth"},
        {"action_name": "Trigger Autonomous Batch", "estimated_duration_sec": 14, "narration_detail": "Click deploy to execute parallel agent jobs.", "ui_element": "deploy-btn"}
    ]
    res = VideoDemoScriptGenerator.generate_demo_script("Batch Orchestrator Agent", steps)
    print("Total chapters:", res["total_chapters"])
    for ch in res["chapters"]:
        print(f"[{ch['timestamp_start']}] {ch['title']}: {ch['narration']}")
