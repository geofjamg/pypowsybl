/**
 * Copyright (c) 2020, RTE (http://www.rte-france.com)
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

package com.powsybl.security;

import java.io.ByteArrayOutputStream;
import java.io.OutputStreamWriter;

import com.powsybl.commons.io.table.AsciiTableFormatterFactory;
import com.powsybl.commons.io.table.TableFormatterConfig;
import com.powsybl.iidm.network.Network;

/**
 * This class hides the access to the Security.print method that is not callable from JPype because print seems to be a reserved keyword
 *
 * @author Mathieu BAGUE {@literal <mathieu.bague at rte-france.com>}
 */
public final class SecurityAnalysisResultPrinter {

    private SecurityAnalysisResultPrinter() {
    }

    public static String toString(SecurityAnalysisResult result, Network network) {
        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        Security.print(result, network, new OutputStreamWriter(bos), new AsciiTableFormatterFactory(), TableFormatterConfig.load());

        return bos.toString();
    }
}
