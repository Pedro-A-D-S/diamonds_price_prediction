from kedro.pipeline import Pipeline, node, pipeline
from .nodes import outlier_removal, drop_duplicates

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func = outlier_removal,
                inputs = 'diamonds',
                outputs = 'outlier_removal_diamonds',
                name = 'outlier_removal_node'
            ),
            node(
                func = drop_duplicates,
                inputs = 'outlier_removal_diamonds',
                outputs = 'diamonds_preprocessed',
                name = 'drop_duplicates_node'
            )
        ],
        name = 'data_processing'
    )
