#!/usr/bin/env python3

import queue
import sys

class Comms:
    def __init__(self):
        self.modules = {}
        self.pulses = None
        self.counts = {False: 0, True: 0}
        self.outputs = {}
        self.inputs = {}

    def add_module(self, module):
        self.modules[module.name] = module

    def add_cable(self, source, destination):
        self.modules[source].add_destination(destination)
        if destination in self.modules:
            self.modules[destination].add_source(source)

    def send_pulse(self, source, destination, value):
        #print(f"{source} -{'high' if value else 'low'}-> {destination}")
        if destination in self.modules:
            if self.modules[destination].receive_pulse(source, value):
                self.pulses.put(destination)
        self.counts[value] += 1

    def push_button(self):
        self.pulses = queue.SimpleQueue()
        self.modules['button'].push()
        while not self.pulses.empty():
            pulse = self.pulses.get()
            self.modules[pulse].send_pulse()

class Module:
    def __init__(self, name, comms):
        self.name = name
        self.comms = comms
        self.sources = []
        self.destinations = []

    def add_source(self, source):
        self.sources.append(source)

    def add_destination(self, destination):
        self.destinations.append(destination)

    def receive_pulse(self, source, value):
        return self._receive_pulse(source, value)

    def _send_pulse(self, value):
        for destination in self.destinations:
            self.comms.send_pulse(self.name, destination, value)

class Button(Module):
    def __init__(self, name, comms):
        super().__init__(name, comms)

    def push(self):
        self._send_pulse(False)

class FlipFlop(Module):
    def __init__(self, name, comms):
        super().__init__(name, comms)
        self.value = False

    def _receive_pulse(self, source, value):
        if not value:
            self.value = not self.value
        return not value

    def send_pulse(self):
        self._send_pulse(self.value)

class Conjunction(Module):
    def __init__(self, name, comms):
        super().__init__(name, comms)
        self.memory = {}

    def add_source(self, source):
        super().add_source(source)
        self.memory[source] = False

    def _receive_pulse(self, source, value):
        self.memory[source] = value
        return True

    def send_pulse(self):
        self._send_pulse(not all(self.memory.values()))

class Broadcast(Module):
    def __init__(self, name, comms):
        super().__init__(name, comms)
        self.value = None

    def _receive_pulse(self, source, value):
        self.value = value
        return True

    def send_pulse(self):
        self._send_pulse(self.value)

def parse_comms(lines):
    comms = Comms()
    button = Button('button', comms)
    comms.add_module(button)
    cables = [('button', 'broadcaster')]
    for line in map(str.strip, lines):
        name, destinations_str = line.split(' -> ')
        destinations = destinations_str.split(', ')
        if name[0] == '%':
            name = name[1:]
            module = FlipFlop(name, comms)
        elif name[0] == '&':
            name = name[1:]
            module = Conjunction(name, comms)
        elif name == 'broadcaster':
            module = Broadcast(name, comms)
        else:
            raise Exception(f"Unknown module type {name!r}")
        comms.add_module(module)
        for destination in destinations:
            cables.append((name, destination))
    for source, destination in cables:
        comms.add_cable(source, destination)
    return comms

if __name__ == '__main__':
    comms = parse_comms(sys.stdin)
    for push in range(1000):
        comms.push_button()
    print(comms.counts[False] * comms.counts[True])
