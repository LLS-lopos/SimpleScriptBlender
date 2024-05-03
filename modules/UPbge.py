import bge

def scene():
    """AI is creating summary for scene

    Returns:
        [None]: [Retourne la scène actuelle.]
    """
    return bge.logic.getCurrentScene()

def objet(nom, valeur=None):
    """AI is creating summary for objet

    Args:
        nom ([str]): [Nom de l'objet à récupérer]
        valeur ([str], optional): [Valeur optionnelle à utiliser]. Defaults to None.

    Returns:
        [bge.types.KX_GameObject]: [L'objet de la scène avec le nom spécifié]
    """
    return scene().objects[nom]


def controlleur():
    """AI is creating summary for controlleur

    Returns:
        [None]: [Retourne le contrôleur actuel]
    """
    return bge.logic.getCurrentController()

def controlleur_actif():
    """AI is creating summary for controlleur_actif

    Returns:
        [None]: [Retourne l'objet propriétaire du contrôleur actuel]
    """
    return controlleur().owner

def capteur(nom):
    """
    Retourne le capteur du contrôleur actuel avec le nom donné.

    Args:
        nom ([str]): Nom du capteur à récupérer.

    Returns:
        [bge.types.SCA_Sensor]: Le capteur du contrôleur actuel avec le nom spécifié.
    """
    return controlleur().sensors[nom]

def control(nom, tache=None):
    if tache is not None:
        if tache == "active":
            return controlleur().activate(actionneur(nom))
    return controlleur().controllers[nom]

def actionneur(nom):
    """
    Retourne l'actionneur du contrôleur actuel avec le nom donné.

    Args:
        nom ([str]): Nom de l'actionneur à récupérer.

    Returns:
        [bge.types.KX_Actuator]: L'actionneur du contrôleur actuel avec le nom spécifié.
    """
    return controlleur().actuators[nom]

def liste(nom):
    """AI is creating summary for liste

    Args:
        nom ([str]): [Nom de la liste à récupérer]
        - objet
        - light
        - camera
        - text
        - brick logic
    Returns:
        [list]: [listes spécifiques de la scène]
        brick logic [dict]: [Dictionnaire contenant les listes de controller, actionneur et capteur de l'objet propriétaire]
    """
    nom = nom.lower()
    if nom == "objet":
        return scene().objects
    elif nom == "light":
        return scene().lights
    elif nom == "camera":
        return scene().cameras
    elif nom == "text":
        return scene().texts
    elif nom == "brick logic":
        brick_list = {"sensors": controlleur_actif().sensors, "controller": controlleur_actif().controllers, "actuator": controlleur_actif().actuators}
        return brick_list


"""
test

a = capteur("b")
b = actionneur("test")
obj = controlleur_actif()
brick = liste("brick logic")

if "b" in brick['sensors'] and "test" in brick['actuator']:
    print("gg")
    if obj:
        print("aussi")
elif a and b in brick:
    print("yep")
else:
    print("n'existe pas")
    print(brick)
    
control("test", "active")
"""