import open3d as o3d
import time

# Create visualizer
vis = o3d.visualization.Visualizer()
vis.create_window(window_name="Real-Time LiDAR Processing")

# Initialize geometries for raw and cleaned clouds
raw_pcd = o3d.geometry.PointCloud()
cleaned_pcd = o3d.geometry.PointCloud()

vis.add_geometry(raw_pcd)
vis.add_geometry(cleaned_pcd)

while True:
    # Step 1: Get new raw point cloud from your LiDAR sensor API
    # For demo: simulate loading a file or generate random cloud
    # Replace this with your actual data stream input:
    pcd = o3d.io.read_point_cloud("path_to_next_frame.pcd")  # Or get from sensor directly

    # Step 2: Clean the point cloud
    cleaned, _ = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)

    # Step 3: Update raw and cleaned clouds in visualizer
    raw_pcd.points = pcd.points
    raw_pcd.colors = pcd.colors if pcd.has_colors() else None
    raw_pcd.paint_uniform_color([1, 1, 1])  # White

    cleaned_pcd.points = cleaned.points
    cleaned_pcd.colors = cleaned.colors if cleaned.has_colors() else None
    cleaned_pcd.paint_uniform_color([1, 0, 0])  # Red

    # Translate for side-by-side view
    raw_pcd.translate((-1.5, 0, 0), relative=False)
    cleaned_pcd.translate((1.5, 0, 0), relative=False)

    vis.update_geometry(raw_pcd)
    vis.update_geometry(cleaned_pcd)
    vis.poll_events()
    vis.update_renderer()

    # Small sleep to control frame rate, adjust as needed
    time.sleep(0.1)
