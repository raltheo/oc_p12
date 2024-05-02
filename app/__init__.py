from app.models.base import Base, engine, SessionLocal
from app.models import Role, Collaborateur, User, Client, Contrat, Evenement
from app.utils.hash_pass import hash_password

def create_tables():
    Base.metadata.create_all(bind=engine)

def create_roles():
    session = SessionLocal()
    roles = {
        "admin": "Responsable de la gestion de la plateforme avec tous les droits d'accès.",
        "commercial": "Gère les interactions avec les clients, les opportunités de vente et les relations clients.",
        "support": "Fournit un soutien lors des événements et gère les aspects logistiques.",
        "gestion": "Gère les aspects financiers et opérationnels de l'entreprise."
    }
    existing_roles = session.query(Role.nom).all()
    existing_roles = [role[0] for role in existing_roles]
    try:
        for role_name, description in roles.items():
            if role_name not in existing_roles:
                new_role = Role(nom=role_name, description=description)
                session.add(new_role)
        session.commit()
    except Exception as e:
        session.rollback()
    finally:
        session.close()

def create_admin():
    session = SessionLocal()
    try:
        admin_role = session.query(Role).filter_by(nom='admin').first()
        admin_user = session.query(User).join(Collaborateur).filter(Collaborateur.role_id == admin_role.roleId).first()
        if not admin_user:
            
            new_user = User(
                nom="Admin",
                email="admin@example.com",
                telephone="1234567890"
            )
            session.add(new_user)
            session.flush() 

            new_collaborateur = Collaborateur(
                userId=new_user.userId,
                role_id=admin_role.roleId,
                password=hash_password("admin").decode()
            )
            session.add(new_collaborateur)
            session.commit()
    except Exception as e:
        session.rollback()
    finally:
        session.close()


def create_collaborator(nom, email, telephone, role_id, password):
    session = SessionLocal()
    try:
        new_user = User(
            nom=nom,
            email=email,
            telephone=telephone
        )
        session.add(new_user)
        session.flush() 

        new_collaborateur = Collaborateur(
            userId=new_user.userId,
            role_id=role_id,
            password=hash_password(password).decode()
        )
        session.add(new_collaborateur)
        session.commit()
    except Exception as e:
        session.rollback()
    finally:
        session.close()

def create_sup_ges_com():
    session = SessionLocal()
    try:
        support_role = session.query(Role).filter_by(nom='support').first()
        commercial_role = session.query(Role).filter_by(nom='commercial').first()
        gestion_role = session.query(Role).filter_by(nom='gestion').first()
    
        support = session.query(User).filter_by(email="support@example.com").first()
        commercial = session.query(User).filter_by(email="commercial@example.com").first()
        gestion = session.query(User).filter_by(email="gestion@example.com").first()
        if not support and support_role: 
            create_collaborator("support", "support@example.com", "1234567890", support_role.roleId, "support")
        if not commercial and commercial_role: 
            create_collaborator("commercial", "commercial@example.com", "1234567890", commercial_role.roleId, "commercial")
        if not gestion and gestion_role: 
            create_collaborator("gestion", "gestion@example.com", "1234567890", gestion_role.roleId, "gestion")
    except:
        pass
            
           

create_tables()
create_roles()
create_admin()
create_sup_ges_com()