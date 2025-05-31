#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

##  MIT License
##
##  Copyright (c) 2024 Bash Club
##
##  Permission is hereby granted, free of charge, to any person obtaining a copy
##  of this software and associated documentation files (the "Software"), to deal
##  in the Software without restriction, including without limitation the rights
##  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
##  copies of the Software, and to permit persons to whom the Software is
##  furnished to do so, subject to the following conditions:
##
##  The above copyright notice and this permission notice shall be included in all
##  copies or substantial portions of the Software.
##
##  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
##  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
##  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
##  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
##  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
##  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
##  SOFTWARE.

from collections.abc import (
    Iterator,
    Sequence,
)

from cmk.server_side_calls.v1 import (
    HostConfig,
    Secret,
    SpecialAgentCommand,
    SpecialAgentConfig,
)

from pydantic import BaseModel

class Params(BaseModel):
    user: str
    password: Secret
    port: int | None = None
    site: str | None = None
    piggyback: str | None = None
    ignore_cert: bool | None = None

def generate_unifi_controller_commands(
    params: Params,
    host_config: HostConfig,
) -> Iterator[SpecialAgentCommand]:
    args: Sequence[str | Secret] = []

    args += [
        '--user', params.user,
        '--password', params.password.unsafe(),
        '--port', str(params.port) if params.port else '443',
        '--piggyback',params.piggyback if params.piggyback else 'hostname',
    ]

    if params.site:
        args += [ "--site", params.site ]
    if params.ignore_cert:
        args += [ "--ignore-cert" ]

    args += [ host_config.primary_ip_config.address or host_config.name]

    yield SpecialAgentCommand(command_arguments=args)

special_agent_unifi_controller = SpecialAgentConfig(
    name="unifi_controller",
    parameter_parser=Params.model_validate,
    commands_function=generate_unifi_controller_commands,
)
