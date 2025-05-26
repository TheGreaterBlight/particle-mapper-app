# particle-mapper-app
A Python 3 desktop application for managing and visualizing particles in 2D space using algorithms like Kruskal, Prim, and nearest neighbor. Developed with PySide2 (Qt for Python), this educational tool allows students to experiment with graph theory, geometry, and data visualization in an interactive environment.

# 💠 Particle Graph Visualizer

A Python 3 + PySide2 (Qt) desktop app for visualizing particles with graph algorithms like Kruskal, Prim, and nearest-neighbor search. Developed as a learning tool for students to explore geometric algorithms, sorting, and graph theory.

---

## 🧰 Features

- 🎯 Add, edit, and visualize particles (2D origin & destination points)
- 📈 Plot colored particle paths with customizable RGB values
- 🧭 Display particle distances and sort by ID, speed, or coordinates
- 🔎 Search particles by ID
- 🧮 Graph construction using:
  - Kruskal’s Algorithm (MST)
  - Prim’s Algorithm (MST)
  - Nearest Neighbor Pairing
- 🖼️ Interactive visual plotting in a second window
- 💾 Save/load particle data to/from JSON

---

## 🖥️ Tech Stack

| Tool           | Purpose                        |
|----------------|--------------------------------|
| Python 3       | Programming Language           |
| PySide2 (Qt)   | GUI Framework (Qt Designer)    |
| QGraphicsScene | 2D drawing for particles/edges |
| JSON           | File I/O for particle data     |
| Custom Classes | Particle, Graph, Utils         |

---

## 📦 How to Install and Run

1. **Clone the project**:

```bash
git clone https://github.com/youruser/particle-graph-visualizer.git
cd particle-graph-visualizer

## 📦 Install Dependencies

```bash
pip install -r requirements.txt

📁 particle-graph-visualizer/
├── main.py                     # App entry point
├── particula.py                # Particle class
├── algoritmos.py               # Algorithms (Kruskal, Prim, Nearest)
├── Utils.py                    # Graph structures, UnionFind, etc.
├── mainwindow.ui               # QtDesigner file for main window
├── graficadorWindow.ui         # QtDesigner file for graph window
├── mainwindow.py               # PySide2 class generated from UI
├── graficadorWindow.py         # PySide2 class generated from UI
└── assets/                     # Optional icons, images
