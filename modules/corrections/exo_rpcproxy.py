# -*- coding: utf-8 -*-

# @BEG@ name=RPCProxy week=6 sequence=2 latex_size=footnotesize no_validation=skip
# une troisième implémentation de RPCProxy

class Forwarder:
    """
    Une instance de la classe Forwarder est un callable
    qui peut être utilisée comme une méthode sur l
    class RPCProxy
    """
    def __init__(self, rpc_proxy, methodname):
        """
        le constructeur  mémorise l'instance de RPCProxy
        et le nom de la méthode qui a été appelée
        """
        self.methodname = methodname
        self.rpc_proxy = rpc_proxy

    def __call__(self, *args):
        """
        en rendant cet objet callable, on peut l'utiliser
        comme une méthode de RPCProxy
        """
        print "Envoi à {}\nde la fonction {} -- args= {}".\
            format(self.rpc_proxy.url, self.methodname, args)
        return "retour de la fonction " + self.methodname

class RPCProxy:
    """
    Une troisième implémentation de RPCProxy qui sous-traite
    à une classe annexe `Forwarder` qui se comporte comme
    une *factory* de méthodes
    """
    def __init__(self, url, login, password):
        self.url = url
        self.login = login
        self.password = password
        
    def __getattr__ (self, methodname):
        """
        Crée à la volée une instance de Forwarder
        correspondant à 'methodname'
        """
        return Forwarder(self, methodname)
# @END@
