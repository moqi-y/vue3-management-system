from sqlalchemy.orm import sessionmaker, exc

from app.sql_app.database import Base, engine
from app.sql_app.models import Role

# 创建数据表
Base.metadata.create_all(engine)

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()


# 查询所有权限
def get_all_roles():
    try:
        roles = session.query(Role).all()
        return [{"id": role.id, "name": role.name, "permissions": role.permissions, "remark": role.remark} for role in
                roles]
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        session.close()


# 新增权限
def insert_role(name, permissions, remark=""):
    perm = Role(name=name, permissions=permissions, remark=remark)
    try:
        session.add(perm)
        session.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
    finally:
        session.close()


# 调用函数新增权限
if __name__ == '__main__':
    #     insert_permission("admin", "查看用户,编辑用户,删除用户", "管理员角色权限")
    print(get_all_roles())
