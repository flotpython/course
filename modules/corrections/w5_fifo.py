from exercice import Args
from exercice_class import ExerciceClass, ScenarioClass

####################
class Fifo(object):

    def __init__(self):
        self.items = []

    def __repr__(self):
        return "<Fifo [{}]>".format(" ".join(["{}".format(i) for i in self.items]))

    def incoming(self, incoming):
        self.items.append(incoming)

    def outgoing(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(0)



scenario1 = ScenarioClass()
scenario1.set_init_args( Args() )
scenario1.add_step( 'incoming', Args(1) )
scenario1.add_step( 'incoming', Args(2) )
scenario1.add_step( 'outgoing', Args() )
scenario1.add_step( 'incoming', Args(3) )
scenario1.add_step( 'incoming', Args(4) )
scenario1.add_step( 'outgoing', Args() )

scenario2 = ScenarioClass()
scenario2.set_init_args(Args ())
scenario1.add_step( 'outgoing', Args() )
scenario2.add_step( 'incoming', Args(1) )
scenario2.add_step( 'incoming', Args(2) )
scenario2.add_step( 'incoming', Args(3) )
scenario2.add_step( 'incoming', Args(4) )
scenario2.add_step( 'outgoing', Args() )

exo_fifo = ExerciceClass (Fifo, [scenario1, scenario2] )

if __name__ == '__main__':
    exo_fifo.correction(Fifo)
                          
