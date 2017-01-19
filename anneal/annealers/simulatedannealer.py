# -*- coding:utf-8 -*-

from .annealer import Annealer


class SimulatedAnnealer(Annealer):
    def __init__(self, model, beta_factor=0.95, freeze_limit=100):
        super().__init__(model)

        self.beta_factor = beta_factor
        self.freeze_limit = freeze_limit
        self.freeze_count = 0
        self.min_energy = self.model.energy

    def is_frozen(self):
        return self.freeze_count >= self.freeze_limit

    def update(self, state_is_updated):
        energy = self.model.energy
        if state_is_updated and energy < self.min_energy:
            self.min_energy = energy
            self.freeze_count = 0
        else:
            self.freeze_count += 1

        self.model.beta /= self.beta_factor
