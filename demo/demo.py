# Copyright (c) 2020, RTE (http://www.rte-france.com)
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import tempfile

from pypowsybl import Network, LoadFlow, LoadFlowParameters
from pypowsybl import ContingencyList, SecurityAnalysis, SecurityAnalysisParameters

network = Network.load("eurostag-tutorial-example1.xml")
print(network.getId())

parameters = LoadFlowParameters.load("lf-parameters.json")
result = LoadFlow.run(network, parameters, "OpenLoadFlow")
print("Computation OK? {}".format(result.isOk()))
print("Metrics: {}".format(result.getMetrics()))

Network.save(network, os.path.join(tempfile.gettempdir(), "eurostag-tutorial-example1-with-loadflow.xml"), "XIIDM")

saParameters = SecurityAnalysisParameters.load("sa-parameters.json")
contingencies = ContingencyList.load("contingencies.groovy")
saResult = SecurityAnalysis.run(network, contingencies, saParameters)
SecurityAnalysis.print(network, saResult)
