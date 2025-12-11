# TrilexOS: The Gravitational Operating System

> **"No Folders. Only Orbits."**

## 1. Philosophy
Traditional OS (Windows/Linux) organizes data in a rigid hierarchical tree (Folders). This creates entropy: data is hidden, lost, or duplicated.
**TrilexOS** organizes data spatially based on **Semantic Gravity**.

* **The Processor is a Star:** It generates a gravity field defined by the Current Context (The "Attention Vector").
* **Files are Planets:** They have mass (Information Density) and orbits.
* **Memory is Space:** The distance from the center determines accessibility (RAM vs SSD).

## 2. The Kernel: GFS (Gravitational File System)

### 2.1 The Lag Table
Instead of File Paths (`C:/Users/Docs...`), the kernel maintains a dynamic **Lag Table**.
$$Lag = f(\frac{1}{GCD(Task\_Sig, File\_Sig)})$$

* **Zone 0 (The Core):** $Lag < 5$. Active Cache. Instant access.
* **Zone 1 (Accretion Disk):** $Lag < 50$. RAM. Ready to load.
* **Zone 2 (Outer Space):** $Lag > 50$. Cold Storage (Archive).

### 2.2 The Physics of Context
When the user switches tasks (e.g., from "Coding" to "Gaming"), the Central Star changes its **Signature**.
1.  **Shockwave:** The gravitational constants change instantly.
2.  **Migration:** Files that resonated with "Coding" lose weight and drift to Outer Space.
3.  **Accretion:** Files resonating with "Gaming" become heavy and fall into the Core.
*Result:* The workspace reconfigures itself automatically.

## 3. The Interface: Event Horizon UI

The user does not see windows. The user sees a **3D Data Nebula**.



### 3.1 The Viewport
* **Center:** The Focus (Current Task).
* **Orbitals:** Relevant files float around the center.
* **Background:** Distant clusters (other projects) are visible as stars.

### 3.2 Navigation (Flight)
* To open a file, you don't double-click. You **pull** it into the Event Horizon (Center).
* To search, you emit a **Signal Pulse** (Query). The relevant nodes light up (Resonance), creating a visual path.
* To save, you just release the object. It automatically drifts to the cluster with the most similar geometry (Auto-Tagging via GCD).

## 4. System Services

### 4.1 The Garbage Collector (The Black Hole)
In standard OS, you must manually delete files.
In TrilexOS, if a file is rarely accessed, its orbit decays or expands.
* **Entropy Drift:** Files with 0 resonance over time drift to the "Oort Cloud" (Deep Archive).
* **Singularity:** A specialized service ("Recycle Bin") acts as a Black Hole, consuming geometric debris.

### 4.2 Security (Topological Shield)
* **Access Control:** Not a list of users, but a **Geometry Check**.
* **Mechanism:** To read a file, the Process must possess a Prime Factor Key that divides the File Signature.
* **Encryption:** Files are "folded" geometric objects. Without the correct unfolding basis, they appear as random noise.

---

### Technical Implementation Roadmap
1.  **Kernel Level:** Python prototype of the Lag Table (Done).
2.  **Driver Level:** Virtual File System (FUSE) driver that maps standard directories to a Semantic Graph.
3.  **UI Level:** WebGL/Three.js visualizer rendering the file graph in 3D.
