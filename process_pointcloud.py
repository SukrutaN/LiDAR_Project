import open3d as o3d
import os

# Step 1: Set the path to your folder
pcd_folder = "C:/Users/Sukruta Nadkarni/OneDrive/Desktop/LiDAR_Project/IITH_LiDAR/raw_data"

# Step 2: Get a list of all .pcd files in that folder
pcd_files = [f for f in os.listdir(pcd_folder) if f.endswith('.pcd')]

# Step 3: Loop through and load each point cloud
raw_point_clouds = []
cleaned_point_clouds = []

for file_name in pcd_files:
    file_path = os.path.join(pcd_folder, file_name)
    pcd = o3d.io.read_point_cloud(file_path)
    raw_point_clouds.append(pcd)

    # Clean point cloud
    cleaned_pcd, _ = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
    cleaned_point_clouds.append(cleaned_pcd)

print(f"Loaded {len(raw_point_clouds)} point clouds.")

# Step 4: Visualize all raw and cleaned clouds side-by-side with spacing
if len(raw_point_clouds) > 0:
    vis = o3d.visualization.Visualizer()
    vis.create_window(window_name="Raw (white) vs Cleaned (red) - Multiple Files", width=1000, height=800)

    spacing = 4  # Distance between pairs
    for i in range(len(raw_point_clouds)):
        raw = raw_point_clouds[i]
        cleaned = cleaned_point_clouds[i]

        raw.paint_uniform_color([1, 1, 1])      # White
        cleaned.paint_uniform_color([1, 0, 0])  # Red

        # Shift raw left, cleaned right, with offset depending on index
        raw.translate((i * spacing * 2 - spacing, 0, 0))
        cleaned.translate((i * spacing * 2 + spacing, 0, 0))

        vis.add_geometry(raw)
        vis.add_geometry(cleaned)

    vis.run()
    vis.destroy_window()
else:
    print("No point clouds to display.")
