import argparse
from userinfo import USERNAME
from pixela_functions import create_graph, update_graph, get_graph_stats, delete_graph

# Argument parser setup
parser = argparse.ArgumentParser(description="Interact with Pixela graphs")
parser.add_argument("-c", "--create", help="Create a new graph", action="store_true")
parser.add_argument("-u", "--update", help="Update an existing graph", action="store_true")
parser.add_argument("-s", "--stats", help="Get statistics of a graph", action="store_true")
parser.add_argument("-g", "--graphid", help="Graph ID to interact with", required=False)
parser.add_argument("-x", "--delete", help="Delete a graph", action="store_true")
args = parser.parse_args()


# Main function to handle commands
def main():
    print(f"Hello {USERNAME} and welcome to the Pixela Habit Tracker!")
    if args.create:
        name = input("Enter the name of the graph: ")
        graph_id = input("Enter the graph ID: ")
        print("Creating graph...")
        print(create_graph(graph_id, name))

    elif args.update:
        if args.graphid:
            quantity = input("Enter the quantity to update: ")
            print("Updating graph...")
            print(update_graph(args.graphid, quantity))
        else:
            print("Graph ID is required for updating a graph.")
    
    elif args.stats:
        if args.graphid:
            print("Fetching graph statistics...")
            print(get_graph_stats(args.graphid))
        else:
            print("Graph ID is required to fetch statistics.")
    
    elif args.delete:
        if args.graphid:
            print("Deleting graph...")
            print(delete_graph(args.graphid))
        else:
            print("Graph ID is required to delete the graph.")

    else:
        print("No action specified. Use -h for help.")

if __name__ == "__main__":
    main()
