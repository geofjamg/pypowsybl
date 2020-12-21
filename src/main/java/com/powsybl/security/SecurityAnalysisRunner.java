/**
 * Copyright (c) 2020, RTE (http://www.rte-france.com)
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

package com.powsybl.security;

import java.util.Objects;

import com.powsybl.commons.PowsyblException;
import com.powsybl.computation.local.LocalComputationManager;
import com.powsybl.contingency.ContingenciesProvider;
import com.powsybl.iidm.network.Network;

/**
 * @author Mathieu BAGUE {@literal <mathieu.bague at rte-france.com>}
 */
public final class SecurityAnalysisRunner {

    private final SecurityAnalysisProvider provider;

    private SecurityAnalysisRunner(SecurityAnalysisProvider provider) {
        this.provider = Objects.requireNonNull(provider);
    }

    public SecurityAnalysisResult run(Network network, ContingenciesProvider contingencies, SecurityAnalysisParameters parameters) {
        return provider.run(network, network.getVariantManager().getWorkingVariantId(), contingencies, parameters, LocalComputationManager.getDefault()).join();
    }

    public static SecurityAnalysisRunner find(String name) {
        if (name == null || name.equals("default")) {
            return new SecurityAnalysisRunner(new DefaultSecurityAnalysisProvider());
        } else if (name.equals("OpenLoadFlow")) {
            return new SecurityAnalysisRunner(new OpenLoadFlowSecurityAnalysisProvider());
        }

        throw new PowsyblException("Unsupported SecurityAnalysis implementation: " + name);
    }

}
