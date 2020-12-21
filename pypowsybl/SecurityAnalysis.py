# Copyright (c) 2020, RTE (http://www.rte-france.com)
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from java.nio.file import Paths

from com.powsybl.contingency import EmptyContingencyListProvider
from com.powsybl.contingency.dsl import GroovyDslContingenciesProvider
from com.powsybl.security import SecurityAnalysisResultPrinter
from com.powsybl.security import SecurityAnalysisRunner
from com.powsybl.security import SecurityAnalysisParameters as JSecurityAnalysisParameters
from com.powsybl.security.json import JsonSecurityAnalysisParameters


class SecurityAnalysis:

    @staticmethod
    def run(network, contingencies=None, parameters=None, implementation=None):
        """
        Run a security analysis
        If the parameters are not passed, the default parameters are loaded from the configuration.
        If several implementation are available, the user has to define the name of the implementation to use

        :param network The IIDM network to compute
        :param contingencies The list of contingencies to simulate
        :param parameters The parameters for the security analysis
        :param implementation The name of the implementation to use

        :return a SecurityAnalysisResult instance
        """
        if parameters is None:
            parameters = JSecurityAnalysisParameters.load()

        return SecurityAnalysisRunner.find(implementation).run(network, contingencies, parameters)

    @staticmethod
    def print(network, result):
        """
        Print a security analysis result

        :param network The network used during the computation
        :param result The result to print
        """
        print(SecurityAnalysisResultPrinter.toString(result, network))


class SecurityAnalysisParameters:

    @staticmethod
    def load(parametersFile=None):
        """
        Load the security analysis parameters from a file
        If the parametersFile is not set, it returns the default parameters loaded from the configuration file

        :param parametersFile The parameters file to load

        :return a SecurityAnalysisParameters instance
        """
        parameters = JSecurityAnalysisParameters.load()
        if parametersFile is not None:
            JsonSecurityAnalysisParameters.update(parameters, Paths.get(parametersFile))

        return parameters

class ContingencyList:

    @staticmethod
    def load(contingenciesFile=None):
        """
        Load a set of contingencies from a file
        If the parametersFile is not set, it returns an empty list of contingencies

        :param parametersFile The parameters file to load

        :return a ContingenciesProvider instance
        """
        if contingenciesFile is None:
            return EmptyContingencyListProvider()
        elif contingenciesFile[-7:] == '.groovy':
            return GroovyDslContingenciesProvider(Paths.get(contingenciesFile))
        else:
            raise NotImplementedError("Unsupported file format: {}".format(contingenciesFile))
