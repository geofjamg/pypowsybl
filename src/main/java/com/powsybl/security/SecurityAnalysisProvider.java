/**
 * Copyright (c) 2020, RTE (http://www.rte-france.com)
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

package com.powsybl.security;

import java.util.concurrent.CompletableFuture;

import com.powsybl.computation.ComputationManager;
import com.powsybl.contingency.ContingenciesProvider;
import com.powsybl.iidm.network.Network;

/**
 * This interface will be integrated in a future version of powsybl-core
 *
 * @author Mathieu BAGUE {@literal <mathieu.bague at rte-france.com>}
 */
public interface SecurityAnalysisProvider {

    public CompletableFuture<SecurityAnalysisResult> run(Network network, String variant, ContingenciesProvider provider, SecurityAnalysisParameters parameters, ComputationManager computationManager);
}
