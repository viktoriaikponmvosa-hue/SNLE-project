from graph import Graph
from bst import BST
from maxheap import MaxHeap
from trie import Trie
from hashmap import HashMap

def main():
    graph = Graph()
    graph.load_network("data/network.txt")

    bst = BST()
    heap = MaxHeap()
    trie = Trie()
    hashmap = HashMap()

    # insert nodes into Trie + HashMap
    for node in graph.adj:
        trie.insert(node)

        hashmap.insert(node, {
            "location": f"Zone {node}",
            "capacity": 100,
            "active": True
        })

    # (optional) cache still kept
    cache = {}

    while True:
        print("\n===== Smart Network Logistics Engine =====")
        print("1. Display Network Summary")
        print("2. Find Shortest Path")
        print("3. Detect Cycles")
        print("4. Dispatch Highest-Priority Package")
        print("5. Search Depot by Name")
        print("6. Autocomplete Depot Name")
        print("7. Exit")
        print("8. Visualize Network (ASCII)")
        print("==========================================")

        choice = input("Choose: ")

        # -----------------------
        # 1. Network Summary
        # -----------------------
        if choice == "1":
            graph.summary()

        # -----------------------
        # 2. Shortest Path (DP version)
        # -----------------------
        elif choice == "2":
            print("Available nodes:", list(graph.adj.keys()))

            s = input("Start: ")
            while s not in graph.adj:
                s = input("Invalid start node. Enter again: ")

            e = input("End: ")
            while e not in graph.adj:
                e = input("Invalid end node. Enter again: ")

            m = input("Mode(distance/time/risk): ").lower()
            while m not in ["distance", "time", "risk"]:
                m = input("Invalid mode. Enter distance/time/risk: ")

            key = (s, e, m)

            if key in cache:
                print("\nUsing cached result...")
                path, cost = cache[key]
            else:
                path, cost = graph.shortest_path(s, e, m)
                cache[key] = (path, cost)

            bst.insert(cost, path)

            if cost == float('inf'):
                print("\nNo path exists between these nodes.")
            else:
                print("\nPath:", " -> ".join(path))
                print("Cost:", cost)

            print("\nSorted Routes (BST):")
            bst.inorder(bst.root)

        # -----------------------
        # 3. Cycle Detection
        # -----------------------
        elif choice == "3":
            print("Cycle exists:", graph.detect_cycle())

        # -----------------------
        # 4. Priority Queue (FIXED)
        # -----------------------
        elif choice == "4":
            package_id = input("Package ID: ")

            priority = input("Priority (1-10): ")
            while not priority.isdigit():
                priority = input("Invalid. Enter numeric priority: ")
            priority = int(priority)

            destination = input("Destination: ")

            weight = input("Weight (kg): ")
            while not weight.replace('.', '', 1).isdigit():
                weight = input("Invalid. Enter numeric weight: ")
            weight = float(weight)

            package = {
                "id": package_id,
                "priority": priority,
                "destination": destination,
                "weight": weight
            }

            heap.enqueue((priority, package))

            print("\nTop Priority Package:", heap.peek())

            if not heap.is_empty():
                dispatched = heap.dequeue()
                print("Dispatched:", dispatched)

        # -----------------------
        # 5. HashMap Search
        # -----------------------
        elif choice == "5":
            name = input("Enter depot name: ")
            result = hashmap.search(name)

            if result:
                print("Depot info:", result)
            else:
                print("Depot not found")

        # -----------------------
        # 6. Trie Autocomplete
        # -----------------------
        elif choice == "6":
            prefix = input("Prefix: ")
            print("Matches:", trie.search_prefix(prefix))

        # -----------------------
        # 7. Exit
        # -----------------------
        elif choice == "7":
            print("Exiting system...")
            break

        # -----------------------
        # 8. ASCII Visualization
        # -----------------------
        elif choice == "8":
            graph.visualize_ascii()

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()