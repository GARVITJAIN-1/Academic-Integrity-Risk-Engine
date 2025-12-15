import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
from networkx.algorithms.community import greedy_modularity_communities

def build_similarity_graph(df_scaled, threshold=0.95):
    sim = cosine_similarity(df_scaled)
    G = nx.Graph()

    for i in range(len(sim)):
        for j in range(i+1, len(sim)):
            if sim[i, j] > threshold:
                G.add_edge(i, j)

    communities = list(greedy_modularity_communities(G))
    community_map = {}

    for idx, community in enumerate(communities):
        for node in community:
            community_map[node] = idx

    similarity_risk = [G.degree(i) if i in G else 0 for i in range(len(sim))]

    return similarity_risk, community_map
