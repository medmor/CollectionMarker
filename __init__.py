bl_info = {
    "name": "Collection Marker Sync",
    "author": "medmor",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "Timeline",
    "description": "Syncs collection visibility with timeline markers",
    "category": "Animation",
}

import bpy

from bpy.app.handlers import persistent

@persistent
def update_collections_by_marker(scene):
    """
    Update collection visibility based on the active timeline marker.
    """
    # Debug: Start of handler
    print(f"\n[CMS] Frame Change Handler - Frame: {scene.frame_current}")

    # Get all markers and sort them by frame number
    markers = sorted(scene.timeline_markers, key=lambda m: m.frame)
    if not markers:
        # Reduced spam: Only print if we expected markers but found none
        # print("[CMS] No markers found in the scene.")
        return

    # Find the most recent marker relative to the current frame
    current_frame = scene.frame_current
    active_marker = None
    
    for marker in markers:
        if marker.frame <= current_frame:
            active_marker = marker
        else:
            break

    # If no marker has been reached yet
    if not active_marker:
        # print("[CMS] No active marker for this frame (before first marker).")
        return

    # print(f"[CMS] Active Marker: '{active_marker.name}' at frame {active_marker.frame}")

    # Iterate through top-level collections in the view layer
    # Note: Using bpy.context in handlers can sometimes be tricky, but frame_change usually works for active viewport.
    # A cleaner way if context fails is getting the view layer from the window manager, but let's debug first.
    try:
        if bpy.context.view_layer:
             view_layer = bpy.context.view_layer
        else:
             # Fallback if context is missing (e.g. rendering)
             return
    except AttributeError:
        # Fallback or error logging if context is restricted
        # print("[CMS] Error: Could not access bpy.context.view_layer")
        return
    
    # Safety check: ensure we are operating on the active scene's view layer
    # We cannot access view_layer.scene directly.
    if bpy.context.scene != scene:
        # The handler is triggering for a scene that is not currently active/visible
        return

    found_match = False
    for layer_col in view_layer.layer_collection.children:
        # Ignore specific collection
        if layer_col.name == "MarkerSyncIgnore":
            continue

        # Exclude if the name doesn't match the active marker's name
        # Set .exclude to True to hide, False to show
        should_exclude = (layer_col.name != active_marker.name)
        
        if not should_exclude:
            found_match = True
        
        # Only update if changed to avoid unnecessary updates/performance hits
        if layer_col.exclude != should_exclude:
            print(f"[CMS] Updating '{layer_col.name}': Exclude = {should_exclude}")
            layer_col.exclude = should_exclude

    if not found_match:
        # print(f"[CMS] WARNING: No collection found matching marker '{active_marker.name}'")
        pass

def register():
    print("\n[CMS] Registering Collection Marker Sync Addon...")
    if update_collections_by_marker not in bpy.app.handlers.frame_change_pre:
        bpy.app.handlers.frame_change_pre.append(update_collections_by_marker)
        print("[CMS] Handler added to frame_change_pre.")
    else:
        print("[CMS] Handler was already registered.")

def unregister():
    print("\n[CMS] Unregistering Collection Marker Sync Addon...")
    if update_collections_by_marker in bpy.app.handlers.frame_change_pre:
        bpy.app.handlers.frame_change_pre.remove(update_collections_by_marker)
        print("[CMS] Handler removed from frame_change_pre.")

if __name__ == "__main__":
    register()
