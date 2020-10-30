# Copyright (c) 2020, RTE (http://www.rte-france.com)
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import jpype
import jpype.imports
import os
import pypowsybl
import tempfile

# Start the JVM before importing java classes
pypowsybl.start()

from pypowsybl import Network, LoadFlow

network = Network.load("eurostag-tutorial-example1.xml")
print(network.getId())

result = LoadFlow.run(network, implementation="OpenLoadFlow")
print("Computation OK? {}".format(result.isOk()))
print("Metrics: {}".format(result.getMetrics()))

Network.save(network, os.path.join(tempfile.gettempdir(), "eurostag-tutorial-example1-with-loadflow.xml"), "XIIDM")

# Shutdown the JVM.
pypowsybl.stop()
