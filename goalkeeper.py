from soccerpy.agent import *
from NeuralNetwork import Brain

class goalkeeper (Agent):
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
            self.wm.teleport_to_point((-5 * side_mod, 30))

        # determina a posicao do gol inimigo
        goal_pos = None
        if self.wm.side == WorldModel.SIDE_R:
            goal_pos = (-55, 0)
        else:
            goal_pos = (55, 0)
        

        stamina = self.wm.get_stamina() / 8000
        kick_bol = self.wm.is_ball_kickable


        print()

if __name__ == "__main__":
    import multiprocessing as mp
    print ("  Spawning agent ...")

    brain = Brain(3, [10, 60], 2)

    at = mp.Process(target=spawn_agent, args=(goalkeeper, "Teste",), kwargs={"brain":brain})
    at.daemon = True
    at.start()

    print ("  Spawned agent ...")

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

