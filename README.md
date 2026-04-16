# Smart Network Logistics Engine (SNLE)

Name: Viktoriia Ikponmvosa  - 300224861
Course: COMP 251
Project: Final Capstone – Smart Network Logistics Engine  

---

## Overview

The Smart Network Logistics Engine (SNLE) is a simulation of a logistics and routing system that integrates multiple data structures and algorithms into one application.

The system models a transportation network as a directed weighted graph where:
- Nodes represent depots or zones
- Edges represent connections between locations
- Each edge includes distance, time, and risk values

The purpose of this project is to apply concepts learned in class, such as graphs, heaps, trees, hashing, and dynamic programming, into a practical system.

---

## Features

### 1. Shortest Path (Dijkstra’s Algorithm)
The program calculates the optimal route between two nodes using Dijkstra’s algorithm.

The user can choose the optimization mode:
- distance
- time
- risk

A custom MinHeap is used for priority queue operations.

---

### 2. Dynamic Programming (Memoization)
The system uses dynamic programming to improve efficiency.

- All-pairs shortest paths are computed using repeated Dijkstra runs
- Results are cached per mode (distance, time, risk)
- Future queries reuse stored results instead of recomputing

---

### 3. Cycle Detection (DFS with Coloring)
Cycle detection is implemented using Depth-First Search.

Each node is assigned a state:
- WHITE: not visited
- GRAY: currently being explored
- BLACK: fully processed

A cycle is detected if a GRAY node is encountered again.

---

### 4. Priority Dispatch Queue (MaxHeap)
A custom MaxHeap is used to simulate a priority queue for package dispatch.

Each package includes:
- package ID
- priority
- destination
- weight

Supported operations:
- enqueue
- dequeue
- peek
- is_empty

The system always dispatches the highest-priority package first.

---

### 5. HashMap (Custom Implementation)
A custom HashMap is implemented using chaining.

- Key: depot name (string)
- Value: depot metadata (location, capacity, active status)

Supported operations:
- insert
- search
- delete
- automatic resizing when load factor exceeds 0.7

---

### 6. Trie (Prefix Search)
A Trie is used to store depot names and support prefix-based search.

Given a prefix, the system returns all matching depot names.

Depth-First Search is used to collect results.

---

### 7. Binary Search Tree (BST)
A Binary Search Tree is used to store computed routes based on cost.

- Each route is inserted into the BST
- Inorder traversal displays routes in sorted order

---

### 8. ASCII Graph Visualization
The system includes an ASCII-based visualization of the network.

It displays:
- nodes
- directed edges
- edge weights (distance, time, risk)

This provides a clear visual representation of the graph structure.

---

## Data Structures Used

- Graph (Adjacency List)
- MinHeap (for Dijkstra’s algorithm)
- MaxHeap (Priority Queue / Dispatch System)
- Trie (Prefix Search)
- Binary Search Tree (BST)
- HashMap (Custom implementation)

---

## Complexity Analysis

### Dijkstra’s Algorithm
Time Complexity: O((V + E) log V)  
Space Complexity: O(V)

---

### Dynamic Programming (Memoization)
Preprocessing: O(V × (V + E) log V)  
Query lookup: O(1)  
Space Complexity: O(V²)

---

### DFS Cycle Detection
Time Complexity: O(V + E)  
Space Complexity: O(V)

---

### MinHeap / MaxHeap
Insert: O(log n)  
Remove: O(log n)

---

### Trie
Insert: O(k)  
Search: O(k)  
(k = length of prefix)

---

### HashMap
Insert/Search/Delete: O(1) average  
Worst case: O(n)

---

### BST
Insert: O(log n) average  
Traversal: O(n)

---

## How to Run

1. Make sure the project structure is:

snle/
├── src/
│   ├── main.py
│   ├── graph.py
│   ├── heap.py
│   ├── hashmap.py
│   ├── trie.py
│   ├── bst.py
│   └── maxheap.py
├── data/
│   └── network.txt
├── README.md
└── requirements.txt

---

2. Run the program:

python src/main.py

---

3. Use the menu to test features such as:
- shortest path
- cycle detection
- package dispatch
- trie search
- visualization

---

## Sample Output

===== Smart Network Logistics Engine =====
1. Display Network Summary
2. Find Shortest Path
3. Detect Cycles
4. Dispatch Highest-Priority Package
5. Search Depot by Name
6. Autocomplete Depot Name
7. Exit
8. Visualize Network (ASCII)
==========================================

Choose: 2

Start: A  
End: D  
Mode: distance  

Path: A -> C -> E -> D  
Cost: 9  

---

## Bonus Features Implemented

- Dynamic Programming (Memoization)
- ASCII Graph Visualization

---

## Notes

- All data structures were implemented manually without using built-in libraries like heapq
- Input validation is included
- The system uses a directed graph as required
- The code is modular and separated into multiple files for clarity

---

## Conclusion

This project demonstrates how multiple data structures and algorithms can be integrated into a single system.

It reinforces key concepts such as graph traversal, priority queues, hashing, trees, and dynamic programming by applying them in a practical context.

Honestly, this project was challenging at times, but it helped me understand the material much better than just doing smaller exercises. Before this, I didn’t fully see how everything connects, but working on this system made it clearer how different data structures actually work together in a real application. It also made me more comfortable with implementing algorithms like Dijkstra and using structures like heaps and trees in a meaningful way.