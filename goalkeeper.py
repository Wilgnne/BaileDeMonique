from soccerpy.agent import *
from NeuralNetwork import Brain, np

class goalkeeper (Agent):
    def __init__(self, brain:Brain):
        super().__init__()
        self.brain = brain
        self.angBuffer = []

    def think(self):
        # take places on the field by uniform number
        if not self.in_kick_off_formation:
        # used to flip x coords for other side
            side_mod = 1
            if self.wm.side == WorldModel.SIDE_R:
                side_mod = -1

            if self.wm.uniform_number == 1:
                self.wm.teleport_to_point((-50 * side_mod, 0))
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
            goal_pos = (-50, 0)
        else:
            goal_pos = (50, 0)

        origem = (goal_pos[0]*-1, goal_pos[1])

        stamina = self.wm.get_stamina()
        stamina = stamina  / 8000 if type(stamina) != type(None) else 0

        kick_bol = int(self.wm.is_ball_kickable())

        view_bol = 1 if self.wm.ball != None else 0

        entry = [stamina, kick_bol, view_bol]

        if self.wm.play_mode == "play_on":
        
            #output = self.brain.think(np.array(entry)).tolist()
            #indexOut = output.index( max(output) )

            # Ficar parado
            #if indexOut == 0:
            #    pass
            

            ang = self.wm.abs_body_dir - self.wm.angle_between_points(self.wm.abs_coords, origem) 

            self.angBuffer.append(ang)
            if len(self.angBuffer) > 10:
                self.angBuffer.pop(0)
            
            ang = sum(self.angBuffer)/len(self.angBuffer)
            print("{:.2f} {}".format(ang, self.wm.get_distance_to_point(origem)))

            if self.wm.get_distance_to_point(origem) > 10:
                if -20 < ang < 20:
                    self.wm.ah.dash(50)
                else:
                    #self.wm.turn_body_to_point(p)
                    t = 5 if ang < 0 else -5
                    self.wm.ah.turn(t)

            pass


if __name__ == "__main__":
    import multiprocessing as mp
    import IO
    print ("  Spawning agent ...")

    agentthreads = []
    for agent in range(1):
        print ("  Spawning agent %d..." % agent)
        brain = None
        #brain = IO.Deserialize("/home/wilgnne/hidden 1/11/30-10-2019 125551.bin")

        at = mp.Process(target=spawn_agent, args=(goalkeeper, "Teste",), kwargs={"brain":brain})
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