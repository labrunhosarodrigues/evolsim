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
    XMOVE =  1,
    YMOVE =  2,
    ATTACK =  3,
    EAT = 4

class Node:
    """
    """

    def __init__(self):
        self.value = 0


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
        source_type = (gene >> 24) & True
        source_node = (gene >> 20) & 0xf
        end_type = (gene >> 19) & True
        end_node = (gene >> 15) & 0xf
        weight = ((gene & 0xefff) / 4000.0) - 4  # weight goes from -4 to 4.192
        
        self.network.append((
            SensorNeurons(source_node) if source_type else InnerNeuron(source_node),
            OutputNeuron(end_node) if end_type else InnerNeuron(source_node),
            weight
        ))

        

