# Collection Marker Sync

A simple yet powerful Blender addon that forces the visibility of your collections to synchronize with your timeline markers. This is essential for scene management, storyboarding, and organizing complex animations where you want to switch between different sets of objects automatically during playback.

## Features
*   **Automatic Synchronization**: Automatically hides/shows collections as the timeline plays or scrubs.
*   **Marker-Based Control**: Uses standard Blender Timeline Markers for intuitive control.
*   **Performance Optimized**: Only updates visibility when the active marker changes.

## Installation

1.  Download this repository.
2.  Place the `CollectionMarker` folder into your Blender addons directory:
    *   **Windows**: `C:\Users\<username>\AppData\Roaming\Blender Foundation\Blender\<version>\scripts\addons\`
    *   **macOS**: `/Users/<username>/Library/Application Support/Blender/<version>/scripts/addons/`
    *   **Linux**: `~/.config/blender/<version>/scripts/addons/`
3.  Open Blender.
4.  Go to **Edit > Preferences > Add-ons**.
5.  Search for **"Collection Marker Sync"**.
6.  Enable the checkbox to activate the addon.

## Usage

1.  **Setup Collections**: Organize your scene into top-level collections (e.g., `Scene_Intro`, `Scene_Action`, `Scene_Ending`).
2.  **Add Markers**: In the Timeline view, move the playhead to the frame where a scene changes and press `M` to add a marker.
3.  **Rename Markers**:
    *   Select the new marker.
    *   Press `Ctrl+M` to rename it.
    *   **Crucial**: The marker name must **exactly match** the name of the Collection you want to show (case-sensitive).
4.  **Animate**: Scrub the timeline or press Play.
    *   When the playhead passes a marker named `Scene_Intro`, the collection `Scene_Intro` becomes **visible**, and all others are **hidden**.

## Troubleshooting
*   **Nothing happens?** Ensure the addon is enabled in Preferences.
*   **Collection won't show?** Check for typos. "Scene 1" is not the same as "Scene_1". The marker name must be identical to the collection name.
*   **Logs**: You can view debug information in the System Console (`Window > Toggle System Console`) to see which markers are being detected.

## Requirements
*   Blender 3.0 or higher.

## Author
medmor
