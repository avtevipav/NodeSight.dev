import plotly.graph_objects as go
import networkx as nx
import math

# Create a new NetworkX graph
G = nx.Graph()

# Add nodes for domains (main cluster 1) with subclusters under Defense Industrial Base (DIB), Bakery, and Healthcare
domainNodes = {
    'gov1': 'Defense Industrial Base (DIB) - Domain 1',
    'gov2': 'Defense Industrial Base (DIB) - Domain 2',
    'gov3': 'Defense Industrial Base (DIB) - Domain 3',
    'bak1': 'Bakery - Domain 1',
    'health1': 'Healthcare - Domain 1',
    'cathAll1': 'Uncat or Unchar - Domain 1',
    'cathAll2': 'Uncat or Unchar - Domain 2',
    'cathAll3': 'Uncat or Unchar - Domain 3',
    'cathAll4': 'Uncat or Unchar - Domain 4',
    'cathAll5': 'Uncat or Unchar - Domain 5',
    'cathAll6': 'Uncat or Unchar - Domain 6',
    'cathAll7': 'Uncat or Unchar - Domain 7',
}

# Add new clusters for Defense Industrial Base (DIB), Bakery, and Healthcare
DomainSubcluster = {
    'DIBsubcluster': 'Critical Infrastructure Sector: Defense Industrial Base (DIB)',
    'bakerySubcluster': 'Bakery',
    'healthcareSubcluster': 'Healthcare',
    'cathAllSubcluster': 'Uncategorized or Uncharacterized',
}

# Add nodes for personas (main cluster 2) with subclusters
personaNodes = {
    'cup1': 'Cupcakers - Persona 1',
    'cup2': 'Cupcakers - Persona 2',
    'cup3': 'Cupcakers - Persona 3',
    'cup4': 'Cupcakers - Persona 4',
    'cup5': 'Cupcakers - Persona 5',
    'cup6': 'Cupcakers - Persona 6',
    'rs1': 'Antidemocratic - Persona 1',
    'rs2': 'Antidemocratic - Persona 2',
    'rs3': 'Antidemocratic - Persona 3',
    'rs4': 'Antidemocratic - Persona 4',
    # 'rs5': 'Antidemocratic - Persona 5',
    # 'rs6': 'Antidemocratic - Persona 6',
    'bicy1': 'Bicycle Polo - Persona 1',
    'bicy2': 'Bicycle Polo - Persona 2',
    'bicy3': 'Bicycle Polo - Persona 3',
    'bicy4': 'Bicycle Polo - Persona 4',
    'bicy5': 'Bicycle Polo - Persona 5',
    # 'bicy6': 'Bicycle Polo - Persona 6',
}

# Add subcluster nodes
PersonaSubcluster = {
    'Pumpernickel Cupcakers': 'Pumpernickel Cupcakers Subcluster',
    'Red Sicle Mallets': 'Red Sicle Mallets Subcluster',
    'Bicycling Croqueters': 'Bicycling Croqueters Subcluster',
}

for node, description in domainNodes.items():
    G.add_node(node, label=description, cluster='domain')

for node, description in DomainSubcluster.items():
    G.add_node(node, label=description, cluster='DomainSubcluster')

G.add_node('domainsMainCluster', label='Domain Names Cluster', cluster='main')

for node, description in personaNodes.items():
    G.add_node(node, label=description, cluster='persona')

for node, description in PersonaSubcluster.items():
    G.add_node(node, label=description, cluster='PersonaSubcluster')

G.add_node('personasMainCluster', label='Persona Main Cluster', cluster='main')

# Connect domain nodes to their respective clusters
G.add_edge('DIBsubcluster', 'gov1')
G.add_edge('DIBsubcluster', 'gov2')
G.add_edge('DIBsubcluster', 'gov3')
G.add_edge('bakerySubcluster', 'bak1')
G.add_edge('healthcareSubcluster', 'health1')
G.add_edge('cathAllSubcluster', 'cathAll1')
G.add_edge('cathAllSubcluster', 'cathAll2')
G.add_edge('cathAllSubcluster', 'cathAll3')
G.add_edge('cathAllSubcluster', 'cathAll4')
G.add_edge('cathAllSubcluster', 'cathAll5')
G.add_edge('cathAllSubcluster', 'cathAll6')
G.add_edge('cathAllSubcluster', 'cathAll7')


# Define relationships between domains and personas
G.add_edge('gov1', 'rs1')
G.add_edge('bak1', 'cup1')
G.add_edge('health1', 'bicy1')
G.add_edge('gov2', 'cup2')
G.add_edge('gov3', 'bicy2')

# Connect the personas to their respective subclusters
G.add_edge('Pumpernickel Cupcakers', 'cup1')
G.add_edge('Pumpernickel Cupcakers', 'cup2')
G.add_edge('Pumpernickel Cupcakers', 'cup3')
G.add_edge('Pumpernickel Cupcakers', 'cup4')
G.add_edge('Pumpernickel Cupcakers', 'cup5')
G.add_edge('Pumpernickel Cupcakers', 'cup6')

G.add_edge('Red Sicle Mallets', 'rs1')
G.add_edge('Red Sicle Mallets', 'rs2')
G.add_edge('Red Sicle Mallets', 'rs3')
G.add_edge('Red Sicle Mallets', 'rs4')
# G.add_edge('Red Sicle Mallets', 'rs5')
# G.add_edge('Red Sicle Mallets', 'rs6')

G.add_edge('Bicycling Croqueters', 'bicy1')
G.add_edge('Bicycling Croqueters', 'bicy2')
G.add_edge('Bicycling Croqueters', 'bicy3')
G.add_edge('Bicycling Croqueters', 'bicy4')
G.add_edge('Bicycling Croqueters', 'bicy5')
# G.add_edge('Bicycling Croqueters', 'bicy6')

# Connect subclusters to the main persona cluster
G.add_edge('personasMainCluster', 'Pumpernickel Cupcakers')
G.add_edge('personasMainCluster', 'Red Sicle Mallets')
G.add_edge('personasMainCluster', 'Bicycling Croqueters')

# Connect the domain clusters to the "Domain Names Cluster"
G.add_edge('domainsMainCluster', 'DIBsubcluster')
G.add_edge('domainsMainCluster', 'bakerySubcluster')
G.add_edge('domainsMainCluster', 'healthcareSubcluster')
G.add_edge('domainsMainCluster', 'cathAllSubcluster')

# Connect personas in the Pumpernickel Cupcakers subcluster
G.add_edge('cup1', 'cup2')
G.add_edge('cup2', 'cup3')
G.add_edge('cup3', 'cup4')
G.add_edge('cup4', 'cup5')
G.add_edge('cup5', 'cup6')

# Connect personas in the Red Sicle Mallets subcluster
G.add_edge('rs1', 'rs2')
G.add_edge('rs2', 'rs3')
G.add_edge('rs3', 'rs4')
# G.add_edge('rs4', 'rs5')
# G.add_edge('rs5', 'rs6')

# Connect personas in the Bicycling Croqueters subcluster
G.add_edge('bicy1', 'bicy2')
G.add_edge('bicy2', 'bicy3')
G.add_edge('bicy3', 'bicy4')
G.add_edge('bicy4', 'bicy5')
# G.add_edge('bicy5', 'bicy6')

# Fixed positions for main clusters and subclusters
fixed_positions = {
    'domainsMainCluster': (-1, 0),
    'DIBsubcluster': (-1.0, 0.25),
    'cathAllSubcluster': (-0.75, 0),
    'bakerySubcluster': (-1.25, 0),
    'healthcareSubcluster': (-1.0, -0.25),
    'personasMainCluster': (1, 0),
    'Pumpernickel Cupcakers': (0.85, 0.20),
    'Red Sicle Mallets': (1.25, 0),
    'Bicycling Croqueters': (0.85, -0.20),
}

# Function to assign positions around a center point
def assign_positions_around(center, node_names, radius=0.1):
    num_nodes = len(node_names)
    positions = {}
    for i, node_name in enumerate(node_names):
        angle = 2 * math.pi * i / num_nodes
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        positions[node_name] = (x, y)
    return positions

# Assign positions for subcluster nodes
subcluster_positions = {}

# For persona subclusters
for subcluster_name, center_node in [('Pumpernickel Cupcakers', 'Pumpernickel Cupcakers'), ('Red Sicle Mallets', 'Red Sicle Mallets'), ('Bicycling Croqueters', 'Bicycling Croqueters')]:
    center = fixed_positions[center_node]
    node_names = [node for node in G.neighbors(subcluster_name) if node in personaNodes]
    positions = assign_positions_around(center, node_names, radius=0.1075)
    subcluster_positions.update(positions)

# For domain subclusters
for subcluster_name, center_node in [('DIBsubcluster', 'DIBsubcluster'), ('bakerySubcluster', 'bakerySubcluster'), ('healthcareSubcluster', 'healthcareSubcluster'), ('cathAllSubcluster', 'cathAllSubcluster')]:
    center = fixed_positions[center_node]
    node_names = [node for node in G.neighbors(subcluster_name) if node in domainNodes]
    positions = assign_positions_around(center, node_names, radius=0.1075)
    subcluster_positions.update(positions)

# Update fixed positions with subcluster positions
fixed_positions.update(subcluster_positions)

# Use fixed positions in the layout
pos = nx.spring_layout(G, pos=fixed_positions, fixed=list(fixed_positions.keys()))

# Identify main cluster nodes
main_cluster_nodes = []
for node in G.nodes(data=True):
    if node[1]['label'] == 'Persona Main Cluster' or node[1]['label'] == 'Domain Names Cluster':
        main_cluster_nodes.append(node[0])

# Create separate edge traces
edge_x_main_clusters = []
edge_y_main_clusters = []

edge_x_others = []
edge_y_others = []

for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    if edge[0] in main_cluster_nodes or edge[1] in main_cluster_nodes:
        edge_x_main_clusters += [x0, x1, None]
        edge_y_main_clusters += [y0, y1, None]
    else:
        edge_x_others += [x0, x1, None]
        edge_y_others += [y0, y1, None]

edge_trace_main_clusters = go.Scatter(
    x=edge_x_main_clusters,
    y=edge_y_main_clusters,
    line=dict(width=1, color='black'),
    hoverinfo='none',
    mode='lines'
)

edge_trace_others = go.Scatter(
    x=edge_x_others,
    y=edge_y_others,
    line=dict(width=1, color='black'),
    hoverinfo='none',
    mode='lines'
)

# Create separate node traces
node_x_main_clusters = []
node_y_main_clusters = []
node_text_main_clusters = []
node_marker_size_main_clusters = []
node_marker_color_main_clusters = []
node_marker_opacity_main_clusters = []

node_x_others = []
node_y_others = []
node_text_others = []
node_marker_size_others = []
node_marker_color_others = []
node_marker_opacity_others = []

for node in G.nodes():
    x, y = pos[node]
    if node in main_cluster_nodes:
        node_x_main_clusters.append(x)
        node_y_main_clusters.append(y)
        node_text_main_clusters.append(G.nodes[node]['label'])
        if G.nodes[node]['label'] == 'Persona Main Cluster':
            node_marker_color_main_clusters.append('purple')
        else:
            node_marker_color_main_clusters.append('teal')
        node_marker_size_main_clusters.append(440)
        node_marker_opacity_main_clusters.append(0.5)
    else:
        node_x_others.append(x)
        node_y_others.append(y)
        node_text_others.append(G.nodes[node]['label'])
        if G.nodes[node]['cluster'] == 'DomainSubcluster':
            node_marker_color_others.append('teal')
            node_marker_size_others.append(120)
            node_marker_opacity_others.append(1)
        elif G.nodes[node]['cluster'] == 'PersonaSubcluster':
            node_marker_color_others.append('purple')
            node_marker_size_others.append(120)
            node_marker_opacity_others.append(1)
        elif G.nodes[node]['cluster'] == 'domain':
            node_marker_color_others.append('lightseagreen')
            node_marker_size_others.append(60)
            node_marker_opacity_others.append(1)
        elif G.nodes[node]['cluster'] == 'persona':
            node_marker_color_others.append('#E0B0FF')
            node_marker_size_others.append(60)
            node_marker_opacity_others.append(1)
        else:
            node_marker_color_others.append('blue')
            node_marker_size_others.append(60)
            node_marker_opacity_others.append(1)

node_trace_main_clusters = go.Scatter(
    x=node_x_main_clusters,
    y=node_y_main_clusters,
    text=node_text_main_clusters,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=False,
        colorscale='YlGnBu',
        size=node_marker_size_main_clusters,
        opacity=node_marker_opacity_main_clusters,
        color=node_marker_color_main_clusters,
    )
)

node_trace_others = go.Scatter(
    x=node_x_others,
    y=node_y_others,
    text=node_text_others,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        colorscale='YlGnBu',
        size=node_marker_size_others,
        opacity=node_marker_opacity_others,
        color=node_marker_color_others,
        colorbar=dict(thickness=15)
    )
)

# Calculate axis ranges to fix the layout
x_values = [pos[node][0] for node in pos]
y_values = [pos[node][1] for node in pos]
margin = 0.2
x_range = [min(x_values) - margin, max(x_values) + margin]
y_range = [min(y_values) - margin, max(y_values) + margin]

# Combine all traces
fig = go.Figure(
    data=[edge_trace_main_clusters, edge_trace_others, node_trace_main_clusters, node_trace_others],
    layout=go.Layout(
        title = "Network Discovery Dashboard: Roles, Relationships, and Analysis (Notional Deliverable Depiction)",
        showlegend=False,
        hovermode='closest',
        dragmode='pan',
        margin=dict(b=0, l=0, r=0, t=40),
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            range=x_range,
            scaleanchor='y',
            scaleratio=1,
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            range=y_range,
        ),
    )
)

# Pulsating effect for main clusters
pulsating_node_indices = []
for idx, text in enumerate(node_trace_main_clusters['text']):
    pulsating_node_indices.append(idx)

# Store the initial sizes of nodes
node_sizes_main_clusters = list(node_trace_main_clusters['marker']['size'])

# Define the sequence of sizes for pulsating effect
pulsate_sizes = [440, 360, 340, 360, 440]

# Create animation frames
frames = []
for i in range(18):  # Number of pulsating cycles
    for size in pulsate_sizes:
        # Copy the node sizes
        frame_node_sizes = list(node_sizes_main_clusters)
        # Update sizes for pulsating nodes
        for idx in pulsating_node_indices:
            frame_node_sizes[idx] = size
        # Create the node_trace for this frame
        frame_node_trace_main_clusters = go.Scatter(
            x=node_trace_main_clusters['x'],
            y=node_trace_main_clusters['y'],
            text=node_trace_main_clusters['text'],
            mode='markers',
            hoverinfo='text',
            marker=dict(
                showscale=False,
                colorscale=node_trace_main_clusters['marker']['colorscale'],
                size=frame_node_sizes,
                opacity=node_trace_main_clusters['marker']['opacity'],
                color=node_trace_main_clusters['marker']['color'],
            )
        )
        frame = go.Frame(
            data=[frame_node_trace_main_clusters],
            traces=[2],  # Index of node_trace_main_clusters in the data list
            name=f'frame_{i}_{size}'
        )
        frames.append(frame)

fig.frames = frames

# Set up the animation settings
fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            showactive=False,
            buttons=[
                dict(
                    label="Animate",
                    method="animate",
                    args=[None, {
                        "frame": {"duration": 200, "redraw": True},
                        "fromcurrent": True,
                        "transition": {"duration": 100, "easing": "quadratic-in-out"},
                        "mode": "immediate",
                        "repeat": True
                    }]
                )
            ],
            x=0.1,
            y=0.05
        ),
        dict(
            buttons=[
                dict(
                    label="Show Main Clusters",
                    method="update",
                    args=[{"visible": [True, True, True, True]}]
                ),
                dict(
                    label="Hide Main Clusters",
                    method="update",
                    args=[{"visible": [False, True, False, True]}]
                ),
            ],
            direction="down",
            showactive=True,
            x=0.1,
            y=0.15
        )
    ]
)

fig.show()
