# -*- coding: utf-8 -*-
"""
Domain Adaptation estimators

"""

# Author: Remi Flamary <remi.flamary@polytechnique.edu>
#         Alexandre Gramfort <firstname.lastname@inria.fr>
#
# License: MIT License

from . import reweight

from .reweight import (
    ReweightDensity, GaussianReweightDensity, ClassifierReweightDensity
)
from .subspace import SubspaceAlignment, TCA

__all__ = [
    "reweight",
    "ReweightDensity",
    "GaussianReweightDensity",
    "ClassifierReweightDensity",
    "SubspaceAlignment",
    "TCA"
]
