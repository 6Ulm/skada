import numpy as np
import pytest
from skada.datasets import make_shifted_blobs


@pytest.fixture(scope="session")
def tmp_da_dataset():
    centers = np.array(
        [
            [0, 0],
            [1, 1],
        ]
    )
    _, n_features = centers.shape

    X, y, X_target, y_target = make_shifted_blobs(
        n_samples=100,
        centers=centers,
        n_features=n_features,
        shift=0.13,
        random_state=42,
        cluster_std=0.05,
    )

    return X, y, X_target, y_target