#include <stdio.h>
#include <stdlib.h>

// Structure to represent a graph node
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Structure to represent a graph
typedef struct Graph {
    int numVertices;
    Node** adjLists;
} Graph;

// Function to create a new graph node
Node* createNode(int data) {
    Node* newNode = (Node*) malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Function to create a graph
Graph* createGraph(int numVertices) {
    Graph* graph = (Graph*) malloc(sizeof(Graph));
    graph->numVertices = numVertices;
    graph->adjLists = (Node**) malloc(numVertices * sizeof(Node*));
    for (int i = 0; i < numVertices; i++) {
        graph->adjLists[i] = NULL;
    }
    return graph;
}

// Function to add an edge to the graph
void addEdge(Graph* graph, int src, int dest) {
    Node* newNode = createNode(dest);
    newNode->next = graph->adjLists[src];
    graph->adjLists[src] = newNode;
}

// Function to perform DFS
void DFS(Graph* graph, int vertex, int* visited) {
    visited[vertex] = 1;
    printf("%d ", vertex);
    Node* temp = graph->adjLists[vertex];
    while (temp) {
        int adjVertex = temp->data;
        if (!visited[adjVertex]) {
            DFS(graph, adjVertex, visited);
        }
        temp = temp->next;
    }
}

// Function to perform BFS
void BFS(Graph* graph, int vertex, int* visited) {
    int queue[graph->numVertices];
    int front = 0, rear = 0;
    queue[rear++] = vertex;
    visited[vertex] = 1;
    while (front < rear) {
        int currVertex = queue[front++];
        printf("%d ", currVertex);
        Node* temp = graph->adjLists[currVertex];
        while (temp) {
            int adjVertex = temp->data;
            if (!visited[adjVertex]) {
                queue[rear++] = adjVertex;
                visited[adjVertex] = 1;
            }
            temp = temp->next;
        }
    }
}

int main() {
    Graph* graph = createGraph(6);
    addEdge(graph, 0, 1);
    addEdge(graph, 0, 2);
    addEdge(graph, 1, 3);
    addEdge(graph, 1, 4);
    addEdge(graph, 2, 5);

    int visited[graph->numVertices];
    for (int i = 0; i < graph->numVertices; i++) {
        visited[i] = 0;
    }

    printf("DFS Traversal: ");
    DFS(graph, 0, visited);
    printf("\n");

    for (int i = 0; i < graph->numVertices; i++) {
        visited[i] = 0;
    }

    printf("BFS Traversal: ");
    BFS(graph, 0, visited);
    printf("\n");

    return 0;
}