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
    """AI is creating summary for creer_armature"""
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

def collection(tache, nom=None):
    """AI is creating summary for collection

    Args:
        tache ([str]): [tache à effectuer pour la catégorie collection]
        nom ([str], optional): [récupère une collection]. Defaults to None.
        - creer
        - recuperer
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

