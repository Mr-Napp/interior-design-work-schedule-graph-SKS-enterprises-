import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# --- Detailed 90-Day Work Schedule ---
tasks = [
    ("Mobilization & Preparation", 1, 10),
    ("Electrical: Conduits/Trays", 11, 20),
    ("Electrical: Cable Pulling", 21, 30),
    ("HVAC: Duct Installation", 11, 25),
    ("HVAC: Equipment Mounting", 26, 35),
    ("Plumbing: Pipe Installation", 16, 30),
    ("Plumbing: Testing & Insulation", 31, 40),
    ("Gypsum: Framing & Boards", 41, 50),
    ("Gypsum: Finishing", 51, 55),
    ("Electrical & Plumbing Fix", 51, 65),
    ("Tile & Stone Fixing", 66, 80),
    ("Final Touch-ups", 81, 85),
    ("Testing & Commissioning", 86, 90),
]

# --- Assign colors per work category ---
colors = {
    "Mobilization & Preparation": "tab:blue",
    "Electrical": "tab:orange",
    "HVAC": "tab:green",
    "Plumbing": "tab:red",
    "Gypsum": "tab:purple",
    "Tile": "tab:brown",
    "Final Touch-ups": "tab:pink",
    "Testing": "tab:gray",
}

# --- Create Gantt Chart ---
fig, ax = plt.subplots(figsize=(12, 8))

yticks = []
yticklabels = []

for i, (task, start, end) in enumerate(tasks):
    # Identify which category color to use
    color_key = next((k for k in colors if k in task), "tab:gray")
    ax.barh(i, end - start + 1, left=start, color=colors[color_key], edgecolor="black")
    yticks.append(i)
    yticklabels.append(task)

# --- Formatting ---
ax.set_yticks(yticks)
ax.set_yticklabels(yticklabels)
ax.set_xlabel("Day")
ax.set_ylabel("Tasks")
ax.set_title("Detailed Interior Fit-Out Work Schedule (90 Days)", fontsize=13, fontweight="bold")
ax.set_xlim(0, 95)
ax.grid(axis="x", linestyle="--", alpha=0.7)
ax.invert_yaxis()  # So earliest tasks are at the top

# --- Legend ---
legend_patches = [mpatches.Patch(color=c, label=k) for k, c in colors.items()]
ax.legend(handles=legend_patches, title="Categories", bbox_to_anchor=(1.05, 1), loc="upper left")

plt.tight_layout()
plt.show()
