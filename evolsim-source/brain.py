# encoding: utf-8
"""
evolsim.brain
-------------

class definition of animal brain from its DNA.
"""

# imports
# built-in
from enum import Enum

# local

# 3rd-party
import numpy as np


class SensorType(Enum):
    AGE = 1,
    XPOS = 2,
    YPOS = 3,


class OutputType(Enum):
    XMOVE = 1,
    YMOVE = 2,
    ATTACK = 3,
    EAT = 4


class Node:
    """
    """

    def __init__(self):
        self.value = 0


class Network:

    def __init__(self, input_nodes=None, middle_nodes=None, output_nodes=None):

        self._inputs = input_nodes
        self._middle = middle_nodes
        self._outputs = output_nodes
        self.inputs_vals = np.zeros(len(input_nodes))
        self.middle_vals = np.zeros(len(middle_nodes))
        self.outputs_vals = np.zero(len(output_nodes))
        self.first_step = np.zeros(self.input.size, self.middle.size)
        self.last_layer = np.zeros(self.middle.size, self.outputs.size)

    def add_connection(self, source, destination, weight):

        if destination in self._outputs:
            self.last_layer[source.value][destination.value] = weight
        else:
            self.first_step[source.value][destination.value] = weight

    def remove_connection(self, source, destination):

        self.add_connection(source, destination, 0)

    def trim_network(self):

        trimmed_inputs = {}
        trimmed_first_step = []
        trimmed_last_layer = []

        for input_node in self._inputs:
            if any(self.first_step[input_node.value][:]):
                trimmed_first_step.append(
                    self.first_step[input_node.value][:]
                )
                trimmed_inputs.add(input_node)
            if any(self.last_layer[input_node.value][:]):
                trimmed_last_layer.append(
                    self.last_layer[input_node.value][:]
                )
                trimmed_inputs.add(input_node)

        for middle_node in self._middle:
            if any(self.first_step[input_node.value][:]):
                trimmed_first_step.append(
                    self.first_step[input_node.value][:]
                )
                trimmed_inputs.add(input_node)
            if any(self.last_layer[input_node.value][:]):
                trimmed_last_layer.append(
                    self.last_layer[input_node.value][:]
                )
                trimmed_inputs.add(input_node)


class Sensor(Node):
    def __init__(self, sensor_type: SensorType):
        self._type = sensor_type

    @property
    def type(self):
        return self._type

    def evaluate(self, inputs):
        self._value = inputs[self._type.value]


class Brain:
    """
    Implementation of animal brain.

    """
    def __init__(self, DNA):
        """
        Initialize brain from DNA.
        """

        brain_DNA = DNA.brain()

        for gene in brain_DNA:
            self.create_connection(gene)

    def create_connection(self, gene):
        # source_type = (gene >> 24) & True
        # source_node = (gene >> 20) & 0xf
        # end_type = (gene >> 19) & True
        # end_node = (gene >> 15) & 0xf
        # weight = ((gene & 0xefff) / 4000.0) - 4
        pass
