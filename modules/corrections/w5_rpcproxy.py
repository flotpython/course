# @BEG@ 5 6 RPCProxy
# une troisième implémentation de RPCProxy

class Forwarder(object):
    def __init__(self, rpc_proxy, function):
        self.function = function
        self.rpc_proxy = rpc_proxy
    # en rendant cet objet callable, on peut l'utiliser
    # comme méthode dans RPCProxy
    def __call__(self, *args):
        print "Envoi à {}\nde la fonction {} -- args= {}".\
            format(self.rpc_proxy.url, self.function, args)
        return "retour de la fonction " + self.function

class RPCProxy(object):
    
    def __init__(self, url, login, password):
        self.url = url
        self.login = login
        self.password = password
        
    def __getattr__ (self, function):
        """
        Crée à la volée une instance de Forwarder
        correspondant à 'function'
        """
        return Forwarder(self, function)

# @END@
