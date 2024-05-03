import math
import random

import bpy
import bpy.types
from mathutils import Vector, Matrix, Euler


#---Debug---#
def debug_test():
    print("from UPbpy import * est OK")


def radian_vers_degres(valeur: float):
    return valeur * (180/math.pi)


def degres_vers_radian(valeur: int):
    return valeur * (math.pi/180)

#---selection---#
def selectionner(valeur=None, objet=None):
    if valeur == "maillages":
        bpy.ops.object.select_by_type(type='MESH')
    elif valeur == "courbes":
        bpy.ops.object.select_by_type(type='CURVE')
    elif valeur == "surfaces":
        bpy.ops.object.select_by_type(type='SURFACE')
    elif valeur == "metaballs":
        bpy.ops.object.select_by_type(type='META')
    elif valeur == "textes":
        bpy.ops.object.select_by_type(type='FONT')
    elif valeur == "courbes de poils":
        bpy.ops.object.select_by_type(type='CURVES')
    elif valeur == "nuages de points":
        bpy.ops.object.select_by_type(type='POINTCLOUD')
    elif valeur == "volumes":
        bpy.ops.object.select_by_type(type='VOLUME')
    elif valeur == "crayons gras":
        bpy.ops.object.select_by_type(type='GPENCIL')
    elif valeur == "armatures":
        bpy.ops.object.select_by_type(type='ARMATURE')
    elif valeur == "lattices":
        bpy.ops.object.select_by_type(type='LATTICE')
    elif valeur == "empty":
        bpy.ops.object.select_by_type(type='EMPTY')
    elif valeur == "lumieres":
        bpy.ops.object.select_by_type(type='LIGHT')
    elif valeur == "sondes lumieres":
        bpy.ops.object.select_by_type(type='LIGHT_PROBE')
    elif valeur == "cameras":
        bpy.ops.object.select_by_type(type='CAMERA')
    elif valeur == "hauts parleurs":
        bpy.ops.object.select_by_type(type='SPEAKER')
    elif valeur == "inverser":
        bpy.ops.object.select_all(action='INVERT')
    elif valeur == "select tous":
        bpy.ops.object.select_all(action='SELECT')
    elif valeur == "deselect tous":
        bpy.ops.object.select_all(action='DESELECT')
    elif valeur == "camera active":
        bpy.ops.object.select_camera()
    elif valeur is None:
        return bpy.context.selected_objects
    elif valeur == "select patern":
        if objet is not None:
            bpy.ops.object.select_pattern('INVOKE_DEFAULT', pattern=objet, case_sensitive=True, extend=True)
    elif valeur == "select":
        if objet is not None:
            selectionner("deselect tous")
            bpy.context.view_layer.objects.active = bpy.data.objects[objet]
            bpy.data.objects[objet].select_set(True)


#---création---#

    

#---parametre de rendu---#
def rendu_image(vue_3D=False):
    bpy.ops.render.render(use_viewport=vue_3D)
    return bpy.data.images['Render Result']


def rendu_animation(vue_3D=False):
    bpy.ops.render.render(animation=True, use_viewport=vue_3D)


#---définir---#
def definir(valeur, objet=None, x=None, y=None, z=None):
    if valeur == "resolution rendu":
        if x is not None and y is not None:
            objet.render.resolution_x = x
            objet.render.resolution_y = y
    elif valeur == "position":
        if x is not None and y is not None and z is not None:
            if objet is not None:
                objet.location = (x, y, z)
            else:
                recuperer().location = (x, y, z)
    elif valeur == "rotation":
        if x is not None and y is not None and z is not None:
            if objet is not None:
                objet.rotation_euler = (x, y, z)
            else:
                recuperer().rotation_euler = (x, y, z)
    elif valeur == "echelle":
        if x is not None and y is not None and z is not None:
            objet.scale = (x, y, z)


def resolution_rendu(x=None, y=None):
    if x and y is not None:
        definir("resolution rendu", x, y)
    else:
        return recuperer("resolution rendu")

#---Texture---#
#---Texte---#


#---récupérer---#
def recuperer(valeur=None, objet=None, condition=False):
    elif valeur == "scene":
        if objet is not None:
            return bpy.data.scenes.get(objet)
        else:
            return bpy.context.scene
    elif valeur == "objet":
        if objet is not None:
            return bpy.data.objects.get(objet)
        if condition == True:
            return bpy.data.objects
        else:
            return bpy.context.active_object
    elif valeur == "position":
        if objet is not None:
            return objet.location
        else:
            return bpy.context.active_object.location
    elif valeur == "dimension":
        if objet is not None:
            return objet.dimensions
        else:
            return bpy.context.active_object.dimensions
    elif valeur == "rotation_euler":
        if objet is not None:
            return objet.rotation_euler
        else:
            return bpy.context.active_object.rotation_euler
    elif valeur == "echelle":
        if objet is not None:
            return objet.scale
        else:
            return bpy.context.active_object.scale
    elif valeur == "nom":
        if objet is not None:
            return objet.name
        else:
            return bpy.context.active_object.name
    elif valeur == "type":
        if objet is not None:
            return objet.type
        else:
            return bpy.context.active_object.type
    elif valeur == "modificateur":
        if objet is not None:
            return list(objet.modifiers)
        else:
            return list(bpy.context.active_object.modifiers)

    elif valeur == "resolution rendu":
        recuplist = []
        recuplist.append(recuperer("scene").render.resolution_x)
        recuplist.append(recuperer("scene").render.resolution_y)
        return recuplist

    elif valeur is None:
        return bpy.context.active_object


def collection_a(valeur, objet, col=None):
    if valeur == "scene":
        return bpy.context.scene.collection.children.link(objet)
    elif valeur == "collection":
        if col is not None:
            return recuperer("collection", col).children.link(objet)


def objet_vers_col(objet, col):
    if objet and col:
        ancien_position = objet.location.copy()
        try:
            bpy.context.scene.collection.objects.unlink(objet)
        except:
            col_actif = bpy.data.objects[objet.name].users_collection[0].name
            recuperer("collection", col_actif).objects.unlink(objet)
        col.objects.link(objet)
        objet.location = ancien_position


def ops_sur(valeur, objet=None):
    if valeur == "scene":
        return bpy.ops.view3d.set_active_collection(is_master_collection=True)
    elif valeur == "toggle mode":
        bpy.ops.object.editmode_toggle()
    elif valeur == "actif":
        return bpy.context.active_object
    elif valeur == "context":
        return bpy.context.object
    elif valeur == "suppr point":
        bpy.ops.curve.delete(type='VERT')


def appliquer(valeur):
    if valeur == "rotation&scale":
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)


#---Modificateur---#
def ajouter(type, valeur, objet=None):
    if type == "contrainte":
        if valeur == "copier position":
            pass
    elif type == "modificateur":
        if valeur == "array":
            pass
    elif type == "particule sys":
        if valeur == "emetteur":
            pass
    elif type == "physique":
        if valeur == "champ de force":
            pass


#---modificateur---#
def ajouterModifierARRAY(nom, fit_type='FIT_CURVE', count=2, use_re_offset=True, re_offset=(1, 0, 0), use_c_offset=False,
                         c_offset=(0, 0, 0), use_merge=False, merge_distance=0.001, curve=None, objet_cible=None):
    """
    Ajoute un modificateur ARRAY à l'objet spécifié(ou actif) avec les options configurables.

    Paramètres :
    - nom : Nom du modificateur ARRAY
    - fit_type : Type d'ajustement ('FIT_CURVE', 'FIT_LENGTH', 'FIXED_COUNT', 'NONE', 'FIT_ARC')
    - count : (Nombre/longueur) d'éléments dans le tableau
    - use_re_offset : Utiliser le décalage relatif entre les éléments du tableau
    - re_offset : Décalage relatif entre les éléments du tableau (tuple de trois valeurs)
    - use_c_offset : Utiliser le décalage constant entre les éléments du tableau
    - c_offset : Décalage constant entre les éléments du tableau (tuple de trois valeurs)
    - use_merge : Fusionne les sommets des éléments adjacents
    - merge_distance : Distance de fusion des sommets
    - curve : Courbe à utiliser pour ajuster le tableau (si fit_type est 'FIT_CURVE')
    - objet_cible : Objet cible pour le tableau (utilisé si le modificateur doit être appliqué à un objet différent de l'objet actif)
    """
    objet_actif = objet_cible if objet_cible else bpy.context.active_object
    if objet_actif is None:
        print("Aucun objet actif n'est sélectionné.")
        return

    modifier_array = objet_actif.modifiers.new(name=nom, type='ARRAY')

    modifier_array.use_relative_offset = use_re_offset
    modifier_array.relative_offset_displace = re_offset

    modifier_array.use_constant_offset = use_c_offset
    modifier_array.constant_offset_displace = c_offset

    modifier_array.use_merge_vertices = use_merge
    modifier_array.merge_threshold = merge_distance

    modifier_array.offset_u = 0
    modifier_array.offset_v = 0
    modifier_array.start_cap = None
    modifier_array.end_cap = None

    modifier_array.fit_type = fit_type
    if fit_type == 'FIT_CURVE':
        if curve is not None:
            modifier_array.curve = curve
    elif fit_type == 'FIXED_COUNT':
        modifier_array.count = count
    elif fit_type == 'FIT_LENGTH':
        modifier_array.fit_length = count
    elif fit_type == 'NONE':
        # Aucun ajustement particulier
        pass
    elif fit_type == 'FIT_ARC':
        modifier_array.fit_arc = count


def ajouterModifierCURVE(nom, axe='POS_X', objet_courbe=None, vertex='', objet_cible=None):
    """
    Ajoute un modificateur CURVE à l'objet spécifié(ou actif) avec les options configurables.

    Paramètres :
    - nom : Nom du modificateur CURVE
    - axe : Axe de déformation ('POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z')
    - objet_courbe : Objet courbe à utiliser comme référence
    - vertex : Groupe de sommets à déformer (nom du vertex group)
    - objet_cible : Objet cible pour le modificateur (utilisé si le modificateur doit être appliqué à un objet différent de l'objet actif)
    """
    objet_actif = objet_cible if objet_cible else bpy.context.active_object
    if objet_actif is None:
        print("Aucun objet actif n'est sélectionné.")
        return

    modifier_curve = objet_actif.modifiers.new(name=nom, type='CURVE')

    modifier_curve.object = objet_courbe
    modifier_curve.deform_axis = axe
    modifier_curve.vertex_group = vertex


def ajouterModifierSIMPLE_DEFORM(nom, methode='TWIST', influence=45, origin=None, axe='X', objet_cible=None):

    objet_actif = objet_cible if objet_cible else bpy.context.active_object
    if objet_actif is None:
        print("Aucun objet actif n'est sélectionné.")
        return

    modifier_simpleDeform = objet_actif.modifiers.new(name=nom, type='SIMPLE_DEFORM')

    if methode == 'TWIST':
        modifier_simpleDeform.angle = degres_vers_radian(influence)
    elif methode == 'BEND':
        modifier_simpleDeform.angle = degres_vers_radian(influence)
    elif methode == 'TAPER':
        modifier_simpleDeform.factor = influence
    elif methode == 'STRETCH':
        modifier_simpleDeform.factor = influence

    modifier_simpleDeform.origin = origin
    modifier_simpleDeform.deform_axis = axe
