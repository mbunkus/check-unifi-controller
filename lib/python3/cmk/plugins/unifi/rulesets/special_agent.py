#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

##  MIT License
##
##  Copyright (c) 2021 Bash Club
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

from cmk.rulesets.v1 import (
    Help,
    Label,
    Title,
)
from cmk.rulesets.v1.form_specs import (
    BooleanChoice,
    DefaultValue,
    DictElement,
    Dictionary,
    Integer,
    Password,
    SingleChoice,
    SingleChoiceElement,
    String,
    migrate_to_password,
    validators,
)
from cmk.rulesets.v1.rule_specs import (
    SpecialAgent,
    Topic,
)

from typing import Mapping

def _valuespec_special_agent_unifi_controller() -> Dictionary:
    return Dictionary(
        title=Title('Unifi Controller via API'),
        help_text=Help('This rule selects the Unifi API agent'),
        elements={
            "user": DictElement(
                parameter_form=String(
                    title=Title("API Username"),
                ),
                required=True,
            ),
            "password": DictElement(
                parameter_form=Password(
                    title=Title("Password"),
                    migrate=migrate_to_password,
                ),
                required=True,
            ),
            "port": DictElement(
                parameter_form=Integer(
                    title=Title("Port"),
                    prefill=DefaultValue(443),
                    custom_validate=(
                        validators.NumberInRange(min_value=1, max_value=65535),
                    ),
                ),
                required=True,
            ),
            "site": DictElement(
                parameter_form=String(
                    title=Title("Site Name"),
                    prefill=DefaultValue("default"),
                ),
                required=False,
            ),
            "ignore_cert": DictElement(
                parameter_form=BooleanChoice(
                    title=Title("Ignore certificate validation"),
                    prefill=DefaultValue(False),
                ),
                required=False,
            ),
            "piggyback": DictElement(
                parameter_form=SingleChoice(
                    title=Title("Receive piggyback data by"),
                    prefill=DefaultValue("name"),
                    elements=[
                        SingleChoiceElement(name="name", title=Title("Hostname")),
                        SingleChoiceElement(name="ip", title=Title("IP")),
                        SingleChoiceElement(name="none", title=Title("None")),
                    ],
                ),
                required=False,
            ),
        },
    )

rule_spec_unifi_controller_special_agent = SpecialAgent(
    name="unifi_controller",
    title=Title("Unifi Controller via API"),
    topic=Topic.NETWORKING,
    parameter_form=_valuespec_special_agent_unifi_controller,
    help_text=Help(
        "This rule selects the Agent Unifi Controller instead of the normal Check_MK Agent "
        "which collects the data through the Unifi Controller REST API"
    ),
)
