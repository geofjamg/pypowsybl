# Copyright (c) 2020, RTE (http://www.rte-france.com)
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from java.nio.file import Paths

from com.powsybl.loadflow import LoadFlow, LoadFlowParameters

def run(network, parameters=None, implementation=None):
    """
    Run a load flow computation
    If the parameters are not passed, the load flow uses the default parameters.
    If several implementation are available, the user has to define the name of the default implementation in the
    configuration file or explicitly pass the name of the implementation to that function.

    :param network The IIDM network to compute
    :param parameters The parameters for the load flow
    :param implementation The name of the load flow simulator to use

    :return a LoadFlowResult instance
    """
    if (parameters is None):
        parameters = LoadFlowParameters.load()

    return LoadFlow.find(implementation).run(network, parameters)
