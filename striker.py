from soccerpy.agent import *
from NeuralNetwork import Brain

import numpy as np

class striker (Agent):
    def __init__(self, brain:Brain):
        super().__init__()
        self.brain = brain

    def think(self):
        # take places on the field by uniform number
        if not self.in_kick_off_formation:
        # used to flip x coords for other side
            side_mod = 1
            if self.wm.side == WorldModel.SIDE_R:
                side_mod = -1

            if self.wm.uniform_number == 1:
                self.wm.teleport_to_point((-5 * side_mod, 30))
            elif self.wm.uniform_number == 2:
                self.wm.teleport_to_point((-40 * side_mod, 15))
            elif self.wm.uniform_number == 3:
                self.wm.teleport_to_point((-40 * side_mod, 00))
            elif self.wm.uniform_number == 4:
                self.wm.teleport_to_point((-40 * side_mod, -15))
            elif self.wm.uniform_number == 5:
                self.wm.teleport_to_point((-5 * side_mod, -30))
            elif self.wm.uniform_number == 6:
                self.wm.teleport_to_point((-20 * side_mod, 20))
            elif self.wm.uniform_number == 7:
                self.wm.teleport_to_point((-20 * side_mod, 0))
            elif self.wm.uniform_number == 8:
                self.wm.teleport_to_point((-20 * side_mod, -20))
            elif self.wm.uniform_number == 9:
                self.wm.teleport_to_point((-10 * side_mod, 0))
            elif self.wm.uniform_number == 10:
                self.wm.teleport_to_point((-10 * side_mod, 20))
            elif self.wm.uniform_number == 11:
                self.wm.teleport_to_point((-10 * side_mod, -20))

            self.in_kick_off_formation = True

            return

        # determina a posicao do gol inimigo
        goal_pos = None
        if self.wm.side == WorldModel.SIDE_R:
            goal_pos = (-60, 0)
        else:
            goal_pos = (60, 0)
        

        stamina = self.wm.get_stamina()
        stamina = stamina  / self.wm.get_stamina_max() if type(stamina) != type(None) else 0

        kick_bol = int(self.wm.is_ball_kickable())

        view_bol = 1 if self.wm.ball != None else 0

        entry = [stamina, kick_bol, view_bol]

        #print("{} entry".format(entry))

        if self.wm.play_mode == "play_on":
        
            output = self.brain.think(np.array(entry)).tolist()
            indexOut = output.index( max(output) )

            # Ficar parado
            if indexOut == 0:
                pass
            # Andar para frente
            elif indexOut == 1:
                self.wm.ah.dash(50)
            # Girar 30 graus
            elif indexOut == 2:
                self.wm.ah.turn(15)
            # Andar em direção a bola
            elif indexOut == 3 and self.wm.ball is not None:
                if self.wm.ball.direction is not None:
                    if -15 <= self.wm.ball.direction <= 15:
                        self.wm.ah.dash(50)
                    else:
                        self.wm.turn_body_to_object(self.wm.ball)
                else:
                    self.wm.ah.turn(15)

            # Chutar a bola
            elif indexOut == 4 and kick_bol:
                #self.wm.turn_body_to_point((goal_pos[0] - 10, 0))
                time.sleep(0.01)
                self.wm.kick_to(goal_pos, 0.0)

def initialize(brain:Brain):
    import multiprocessing as mp
    print ("  Spawning agent ...")

    spawn_agent(striker, "Teste", brain=brain)


'''
if __name__ == "__main__":
    import multiprocessing as mp
    import IO
    print ("  Spawning agent ...")

    agentthreads = []
    for agent in range(2):
        print ("  Spawning agent %d..." % agent)

        brain = IO.Deserialize("/home/wilgnne/teste/11/12-11-2019 01:30:37.bin")

        at = mp.Process(target=spawn_agent, args=(striker, "Teste",), kwargs={"brain":brain})
        at.daemon = True
        at.start()

        agentthreads.append(at)

    # aguarde até que seja morto para finalizar os processos do agente
    try:
        while 1:
            time.sleep(0.05)
    except KeyboardInterrupt:
        print ()
        print ("Killing agent thread...")

        print ("  Terminating agent %d..." % count)
        at.terminate()

        print ("Exiting.")
        sys.exit()

'''