"""Multimodal Video Demo Script & Narration Generator.
100% Python Standard Library.
"""

class VideoDemoScriptGenerator:
    """Transforms UI workflow action sequences into structured video demo chapters and narration scripts."""
    
    @staticmethod
    def generate_demo_script(workflow_title: str, steps: list) -> dict:
        chapters = []
        total_seconds = 0
        
        chapters.append({
            "chapter_index": 1,
            "title": "Introduction & Overview",
            "timestamp_start": "00:00",
            "duration_sec": 8,
            "narration": f"Welcome! In this quick walkthrough, we'll demonstrate how {workflow_title} automates end-to-end tasks with zero friction.",
            "visual_cue": "Show product dashboard and high-level workflow architecture."
        })
        total_seconds += 8
        
        for idx, step in enumerate(steps, start=2):
            dur = step.get("estimated_duration_sec", 10)
            start_m, start_s = divmod(total_seconds, 60)
            narration = (
                f"Next, step {idx - 1}: {step.get('action_name', 'execute step')}. "
                f"{step.get('narration_detail', 'The agent inspects parameters and verifies execution integrity.')}"
            )
            chapters.append({
                "chapter_index": idx,
                "title": step.get("action_name", f"Step {idx - 1}"),
                "timestamp_start": f"{start_m:02d}:{start_s:02d}",
                "duration_sec": dur,
                "narration": narration,
                "visual_cue": f"Highlight {step.get('ui_element', 'active UI viewport')} with cursor zoom."
            })
            total_seconds += dur
            
        out_m, out_s = divmod(total_seconds, 60)
        chapters.append({
            "chapter_index": len(steps) + 2,
            "title": "Summary & Next Steps",
            "timestamp_start": f"{out_m:02d}:{out_s:02d}",
            "duration_sec": 7,
            "narration": f"And that's how {workflow_title} completes the pipeline in seconds. Try it today or connect with our team for custom agent workflows.",
            "visual_cue": "Display call-to-action button and API documentation link."
        })
        total_seconds += 7
        
        return {
            "workflow": workflow_title,
            "total_duration_sec": total_seconds,
            "total_chapters": len(chapters),
            "chapters": chapters
        }
