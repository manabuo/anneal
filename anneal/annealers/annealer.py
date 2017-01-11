# -*- coding:utf-8 -*-

import abc
import math
import random


class Annealer(metaclass=abc.ABCMeta):
    def initialize(self, initial_state):
        self.step_count = 0
        self.current_state = initial_state
        self.current_energy = self.energy(initial_state)

    def update(self, state, energy):
        self.current_state = state
        self.current_energy = energy

    def count_up(self, prev_state, prev_energy):
        self.step_count += 1

    def is_acceptable(self, candidate_energy):
        delta = max(0.0, candidate_energy - self.current_energy)
        return math.exp(-delta) >= random.random()

    @abc.abstractmethod
    def energy(self, state):
        pass

    @abc.abstractmethod
    def get_neighbor(self, state):
        pass

    @abc.abstractmethod
    def is_frozen(self):
        pass

    def anneal(self, **kwargs):
        return self.optimize(**kwargs)

    def optimize(self, initial_state=None):
        self.initialize(initial_state)

        while not self.is_frozen():
            candidate_state = self.get_neighbor(self.current_state)
            candidate_energy = self.energy(candidate_state)
            if self.is_acceptable(candidate_energy):
                self.update(candidate_state, candidate_energy)
            self.count_up(candidate_state, candidate_energy)

        return self.state
