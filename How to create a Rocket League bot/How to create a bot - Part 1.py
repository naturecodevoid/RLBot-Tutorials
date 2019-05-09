from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.structures.game_data_struct import GameTickPacket

class PythonExample(BaseAgent):

    def get_output(self, packet: GameTickPacket) -> SimpleControllerState:
        self.controller = SimpleControllerState()
        self.controller.throttle = 1

        return self.controller
