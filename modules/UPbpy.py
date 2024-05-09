import bpy

def creer_primitive(nom):
    """AI is creating summary for creer_primitive

    Args:
        nom ([str]): [nom de l'objet primitive à créer]
        - plan
        - cube
        - cercle
        - sphere
        - icosphere
        - cylindre
        - cone
        - tore
        - grille
        - singe
    """
    nom = nom.lower()
    if nom == "plan":
        bpy.ops.mesh.primitive_plane_add()
    elif nom == "cube":
        bpy.ops.mesh.primitive_cube_add()
    elif nom == "cercle":
        bpy.ops.mesh.primitive_circle_add()
    elif nom == "sphere":
        bpy.ops.mesh.primitive_uv_sphere_add()
    elif nom == "icosphere":
        bpy.ops.mesh.primitive_ico_sphere_add()
    elif nom == "cylindre":
        bpy.ops.mesh.primitive_cylinder_add()
    elif nom == "cone":
        bpy.ops.mesh.primitive_cone_add()
    elif nom == "tore":
        bpy.ops.mesh.primitive_torus_add()
    elif nom == "grille":
        bpy.ops.mesh.primitive_grid_add()
    elif nom == "singe":
        bpy.ops.mesh.primitive_monkey_add()

def creer_courbe(nom):
    """AI is creating summary for creer_courbe

    Args:
        nom ([str]): [nom de l'objet primitive courbe à créer]
        - bezier
        - cercle
        - nurbs
        - nurbs cercle
        - chemin
        - poil
        - fourrure
    """
    nom = nom.lower()
    if nom == "bezier":
        bpy.ops.curve.primitive_bezier_curve_add()
    elif nom == "cercle":
        bpy.ops.curve.primitive_bezier_circle_add()
    elif nom == "nurbs":
        bpy.ops.curve.primitive_nurbs_curve_add()
    elif nom == "nurbs cercle":
        bpy.ops.curve.primitive_nurbs_circle_add()
    elif nom == "chemin":
        bpy.ops.curve.primitive_nurbs_path_add()
    elif nom == "poil":
        bpy.ops.object.curves_empty_hair_add()
    elif nom == "fourrure":
        bpy.ops.object.quick_fur()

def creer_surface(nom):
    """AI is creating summary for creer_surface

    Args:
        nom ([str]): [nom de l'objet primitive surface à créer]
        - courbe
        - cercle
        - surface
        - cylindre
        - sphere
        - tore
    """
    nom = nom.lower()
    if nom == "courbe":
        bpy.ops.surface.primitive_nurbs_surface_curve_add()
    elif nom == "cercle":
        bpy.ops.surface.primitive_nurbs_surface_circle_add()
    elif nom == "surface":
        bpy.ops.surface.primitive_nurbs_surface_surface_add()
    elif nom == "cylindre":
        bpy.ops.surface.primitive_nurbs_surface_cylinder_add()
    elif nom == "sphere":
        bpy.ops.surface.primitive_nurbs_surface_sphere_add()
    elif nom == "tore":
        bpy.ops.surface.primitive_nurbs_surface_torus_add()

def creer_metaballe(nom):
    """AI is creating summary for creer_metaballe

    Args:
        nom ([str]): [nom de l'objet metaball à créer]
        - balle
        - capsule
        - plan
        - ellipsoide
        - cube
    """
    nom = nom.lower()
    if nom == "balle":
        bpy.ops.object.metaball_add(type='BALL')
    elif nom == "capsule":
        bpy.ops.object.metaball_add(type='CAPSULE')
    elif nom == "plan":
        bpy.ops.object.metaball_add(type='PLANE')
    elif nom == "ellipsoide":
        bpy.ops.object.metaball_add(type='ELLIPSOID')
    elif nom == "cube":
        bpy.ops.object.metaball_add(type='CUBE')

def creer_texte():
    """AI is creating summary for creer_texte"""
    bpy.ops.object.text_add()

def creer_volume():
    """AI is creating summary for creer_volume"""
    bpy.ops.object.volume_add()

def creer_crayon_gras(nom):
    """AI is creating summary for creer_crayon_gras

    Args:
        nom ([str]): [nom de l'objet crayon gras à créer]
        - vide
        - trait
        - singe
        - scene
        - collection
        - objet
    """
    nom = nom.lower()
    if nom == "vide":
        bpy.ops.object.gpencil_add(type='EMPTY')
    elif nom == "trait":
        bpy.ops.object.gpencil_add(type='STROKE')
    elif nom == "singe":
        bpy.ops.object.gpencil_add(type='MONKEY')
    elif nom == "scene":
        bpy.ops.object.gpencil_add(type='LRT_SCENE')
    elif nom == "collection":
        bpy.ops.object.gpencil_add(type='LRT_COLLECTION')
    elif nom == "objet":
        bpy.ops.object.gpencil_add(type='LRT_OBJECT')

def creer_armature():
    """AI is creating summary for creer_armature

    simple os
    """
    bpy.ops.object.armature_add()
    
def creer_lattice():
    """AI is creating summary for creer_lattice"""
    bpy.ops.object.add(type='LATTICE')

def creer_vide(nom):
    """AI is creating summary for creer_vide

    Args:
        nom ([str]): [nom de l'objet empty à créer]
        - simple
        - fleche
        - fleche unique
        - cercle
        - cube
        - sphere
        - cone
        - image
    """
    nom = nom.lower()
    if nom == "simple":
        bpy.ops.object.empty_add(type='PLAIN_AXES')
    elif nom == "fleche":
        bpy.ops.object.empty_add(type='ARROWS')
    elif nom == "fleche unique":
        bpy.ops.object.empty_add(type='SINGLE_ARROW')
    elif nom == "cercle":
        bpy.ops.object.empty_add(type='CIRCLE')
    elif nom == "cube":
        bpy.ops.object.empty_add(type='CUBE')
    elif nom == "sphere":
        bpy.ops.object.empty_add(type='SPHERE')
    elif nom == "cone":
        bpy.ops.object.empty_add(type='CONE')
    elif nom == "image":
        bpy.ops.object.empty_add(type='IMAGE')

def creer_image(nom):
    """AI is creating summary for creer_image

    Args:
        nom ([str]): [nom de l'objet image à créer]
        - image reference
        - image arriere plan
    """
    nom = nom.lower()
    if nom == "image reference":
        bpy.ops.object.load_reference_image()
    elif nom == "image arriere plan":
        bpy.ops.object.load_background_image()
    
def creer_eclairage(nom):
    """AI is creating summary for creer_eclairage

    Args:
        nom ([str]): [nom de l'objet light à créer]
        - point
        - soleil
        - spot
        - zone
    """
    nom = nom.lower()
    if nom == "point":
        bpy.ops.object.light_add(type='POINT')
    elif nom == "soleil":
        bpy.ops.object.light_add(type='SUN')
    elif nom == "spot":
        bpy.ops.object.light_add(type='SPOT')
    elif nom == "zone":
        bpy.ops.object.light_add(type='AREA')

def creer_sonde_lumiere(nom):
    """AI is creating summary for creer_sonde_lumiere

    Args:
        nom ([str]): [nom de l'objet sonde lumière à créer]
        - cubemap
        - plan
        - volume irradiant
    """
    nom = nom.lower()
    if nom == "cubemap":
        bpy.ops.object.lightprobe_add(type='CUBEMAP')
    elif nom == "plan":
        bpy.ops.object.lightprobe_add(type='PLANAR')
    elif nom == "volume irradiant":
        bpy.ops.object.lightprobe_add(type='GRID')

def creer_camera():
    """AI is creating summary for creer_camera"""
    bpy.ops.object.camera_add()

def creer_haut_parleur():
    """AI is creating summary for creer_haut_parleur"""
    bpy.ops.object.speaker_add()

def creer_force(nom):
    """AI is creating summary for creer_force

    Args:
        nom ([str]): [nom de l'objet force à créer]
        - force
        - vent
        - tourbillon
        - magnetique
        - harmonique
        - charge
        - lennard jones
        - texture
        - guide courbe
        - boid
        - turbulence
        - trainer
        - flux fluide
    """
    nom = nom.lower()
    if nom == "force":
        bpy.ops.object.effector_add(type='FORCE')
    elif nom == "vent":
        bpy.ops.object.effector_add(type='WIND')
    elif nom == "tourbillon":
        bpy.ops.object.effector_add(type='VORTEX')
    elif nom == "magnetique":
        bpy.ops.object.effector_add(type='MAGNET')
    elif nom == "harmonique":
        bpy.ops.object.effector_add(type='HARMONIC')
    elif nom == "charge":
        bpy.ops.object.effector_add(type='CHARGE')
    elif nom == "lennard jones":
        bpy.ops.object.effector_add(type='LENNARDJ')
    elif nom == "texture":
        bpy.ops.object.effector_add(type='TEXTURE')
    elif nom == "guide courbe":
        bpy.ops.object.effector_add(type='GUIDE')
    elif nom == "boid":
        bpy.ops.object.effector_add(type='BOID')
    elif nom == "turbulence":
        bpy.ops.object.effector_add(type='TURBULENCE')
    elif nom == "trainer":
        bpy.ops.object.effector_add(type='DRAG')
    elif nom == "flux fluide":
        bpy.ops.object.effector_add(type='FLUID')

def collection(tache, nom=None, col=None):
    """AI is creating summary for collection

    Args:
        tache ([str]): [tache à effectuer pour la catégorie collection]
        nom ([str], optional): [récupère une collection]. Defaults to None.
        - creer
        - recuperer
        - dans scene
        - dans collection
        - assigne objet
    Returns:
        [bpy.data.collections.new]: [création d'une nouvelle collection]
        [str: bpy.data.collections.get()]: récupère une collection si elle existe
    """
    tache = tache.lower()
    if tache == "creer":
        if nom is not None:
            return bpy.data.collections.new(nom)
        else:
            return bpy.data.collections.new("Collection")
    elif tache == "recuperer" and nom is not None:
        return bpy.data.collections.get(nom, "n'existe pas")
    elif tache == "dans scene" and nom is not None:
        return scene(valeur="actif").collection.children.link(nom)
    elif tache == "dans collection":
        if nom and col is not None:
            return bpy.data.collections[col].children.link(nom)
    elif tache == "assigne objet":
        if nom and col is not None:
            obj = bpy.data.objects[nom]
            ancien_position = obj.location.copy()
            try:
                scene(valeur="actif").collections.objects.unlink(obj)
            except:
                col_actif = obj.users_collection[0].name
                bpy.data.collections.get(col_actif, "non existent")
            col.objects.link(obj)
            obj.location = ancien_position

def environnement(tache, nom=None):
    """AI is creating summary for environnement

    Args:
        tache ([str]): [tache à effectuer pour la catégorie environnement]
        nom ([str], optional): [valeur optionnel]. Defaults to None.
        - creer
    """
    tache = tache.lower()
    if tache == "creer":
        bpy.ops.world.new()

def materiau(tache, nom=None):
    """AI is creating summary for materiau

    Args:
        tache ([str]): [tache à effectuer pour la catégorie matériau]
        nom ([str], optional): [valeur optionnel]. Defaults to None.
        - creer
    """
    tache = tache.lower()
    if tache == "creer":
        bpy.ops.material.new()

def moteur_rendu(nom):
    """AI is creating summary for moteur_rendu

    Args:
        nom ([str]): [moteur de rendu à activé]
        - eevee
        - cycles
    """
    nom = nom.lower()
    if nom == "eevee":
        bpy.context.scene.render.engine = 'BLENDER_EEVEE'
    elif nom == "cycles":
        bpy.context.scene.render.engine = 'CYCLES'

def liste(nom):
    """AI is creating summary for liste

    Args:
        nom ([str]): [nom de la liste à récupérer]
        - armature
        - objet
        - collection
        - camera
        - brosse
        - courbe
        - image
        - lattice
        - lumiere
        - materiau
        - mesh
        - metaball
        - node group
        - texte
        - texture
        - scene
    Returns:
        [list]: [retourne la liste d'élément rechercher]
    """
    nom = nom.lower()
    if nom == "armature":
        return list(bpy.data.armatures)
    elif nom == "objet":
        return list(bpy.data.objects)
    elif nom == "collection":
        return list(bpy.data.collections)
    elif nom == "camera":
        return list(bpy.data.cameras)
    elif nom == "brosse":
        return list(bpy.data.brushes)
    elif nom == "courbe":
        return list(bpy.data.curves)
    elif nom == "image":
        return list(bpy.data.images)
    elif nom == "lattice":
        return list(bpy.data.lattices)
    elif nom == "lumiere":
        return list(bpy.data.lights)
    elif nom == "materiau":
        return list(bpy.data.materials)
    elif nom == "mesh":
        return list(bpy.data.meshes)
    elif nom == "metaball":
        return list(bpy.data.metaballs)
    elif nom == "node group":
        return list(bpy.data.node_groups)
    elif nom == "texte":
        return list(bpy.data.texts)
    elif nom == "texture":
        return list(bpy.data.textures)
    elif nom == "scene":
        return list(bpy.data.scenes)

def selection(nom, valeur=None):
    nom = nom.lower()
    if valeur is not None:
        valeur = valeur.lower()
    if nom == "tout":
        bpy.ops.object.select_all(action='SELECT')
    elif nom == "aucun":
        bpy.ops.object.select_all(action='DESELECT')
    elif nom == "inverse":
        bpy.ops.object.select_all(action='INVERT')
    elif nom == "rectangle":
        bpy.ops.view3d.select_box()
    elif nom == "cercle":
        bpy.ops.view3d.select_circle()
    elif nom == "lasso":
        if valeur is not None:
            if valeur == "definir":
                bpy.ops.view3d.select_lasso(mode='SET')
            elif valeur == "etendre":
                bpy.ops.view3d.select_lasso(mode='ADD')
            elif valeur == "soustraire":
                bpy.ops.view3d.select_lasso(mode='SUB')
            elif valeur == "difference":
                bpy.ops.view3d.select_lasso(mode='XOR')
            elif valeur == "intersection":
                bpy.ops.view3d.select_lasso(mode='AND')
    elif nom == "type":
        if valeur is not None:
            if valeur == "maillage":
                bpy.ops.object.select_by_type(type='MESH')
            elif valeur == "courbe":
                bpy.ops.object.select_by_type(type='CURVE')
            elif valeur == "surface":
                bpy.ops.object.select_by_type(type='SURFACE')
            elif valeur == "metaball":
                bpy.ops.object.select_by_type(type='META')
            elif valeur == "texte":
                bpy.ops.object.select_by_type(type='FONT')
            elif valeur == "courbe poil":
                bpy.ops.object.select_by_type(type='CURVES')
            elif valeur == "nuage point":
                bpy.ops.object.select_by_type(type='POINTCLOUD')
            elif valeur == "volume":
                bpy.ops.object.select_by_type(type='VOLUME')
            elif valeur == "crayon gras":
                bpy.ops.object.select_by_type(type='GPENCIL')
            elif valeur == "armature":
                bpy.ops.object.select_by_type(type='ARMATURE')
            elif valeur == "lattice":
                bpy.ops.object.select_by_type(type='LATTICE')
            elif valeur == "vide":
                bpy.ops.object.select_by_type(type='EMPTY')
            elif valeur == "eclairage":
                bpy.ops.object.select_by_type(type='LIGHT')
            elif valeur == "sonde lumiere":
                bpy.ops.object.select_by_type(type='LIGHT_PROBE')
            elif valeur == "camera":
                bpy.ops.object.select_by_type(type='CAMERA')
            elif valeur == "haut parleur":
                bpy.ops.object.select_by_type(type='SPEAKER')
    elif nom == "camera actif":
        bpy.ops.object.select_camera()
    elif nom == "miroir":
        bpy.ops.object.select_mirror()
    elif nom == "aleatoire":
        bpy.ops.object.select_random()
    elif nom == "objet":
        if valeur is not None:
            bpy.data.objects[valeur].name
        else:
            return bpy.context.active_object

def scene(valeur, nom=None):
    if valeur == "actif":
        return bpy.context.scene
    elif nom is not None:
        nom = nom.lower()
        if valeur == "scene":
            return bpy.data.scenes.get(nom, "erreur")

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

#------#

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

def appliquer(valeur):
    if valeur == "rotation&scale":
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
