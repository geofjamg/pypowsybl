# Copyright (c) 2020, RTE (http://www.rte-france.com)
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from java.nio.file import Paths

from com.powsybl.iidm.export import Exporters
from com.powsybl.iidm.importers import Importers


class Network:

    @staticmethod
    def load(filename):
        """
        Create an IIDM network from a case file

        :param filename The name of the case file to load

        :return an IIDM network
        """
        return Importers.loadNetwork(filename)

    @staticmethod
    def save(network, filename, format):
        """
        Save an IIDM network to a case file, in the specified format

        :param network The IIDM network to save
        :param filename The filename of the case file to write
        :param format The format of the case file
        """
        Exporters.export(format, network, None, Paths.get(filename))
