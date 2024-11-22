import graphistry

# Graphistry initialization
graphistry.register(api=3, personal_key_id='CZSF3TG59H', personal_key_secret='IEYZ2FWQ6FW436FR')


def run_filters(df):
    """
    Creates a graph with default settings for Graphistry.
    """
    graph_url = (
        graphistry.edges(df)
        .bind(source="source", destination="target")
        .settings(url_params={'linLog': True, 'strongGravity': False, 'dissuadeHubs': True, 'play': 4000})
        .plot(render=False)
    )
    return graph_url
