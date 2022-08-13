from database import engine, Base, session
from models import User, UserProfile

if __name__ == "__main__":

    # Cria as tabelas definidas no módulo models.py
    Base.metadata.create_all(engine)

    # O método all() trás todos os registros da tabela mapeada para a model passada
    # como argumento de query(). No exemplo abaixo, é a model User.
    # SELECT * FROM tb_users
    result = session.query(User).all()

    print(f"Quantidade de registros na tabela tb_users: {len(result)}")

    users = [
        {"first_name": "Amanda", "last_name": "dos Anjos", "email": "amanda@email.com", "password": "123456"},
        {"first_name": "Bruna", "last_name": "Silva", "email": "bruna@email.com", "password": "123456"},
        {"first_name": "Carla", "last_name": "da Silva", "email": "carla@email.com", "password": "123456"},
    ]

    # Só iremos inserir os dados se não houverem registros na tabela tb_users
    if len(result) == 0:
        for user_info in users:

            # Instanciamos a classe User passando os valores para os campos dessa classe
            user = User(email=user_info.get("email"), password=user_info.get("password"))

            # Adicionamos o objeto à sessão (ainda não está salvo na tabela)
            session.add(user)

            # Confirma a adição dos dados na tabela
            session.commit()

            user_profile = UserProfile(
                id=user.id,
                first_name=user_info.get("first_name"),
                last_name=user_info.get("last_name")
            )

            session.add(user_profile)
            session.commit()

    elif len(result) > 0:
        users = session.query(User).all()

        """
        Nesse caso, se quisermos mostrar os dados de usuário e os dados de perfil de usuário, temos que
        chamar a model UserProfile passando o id do usuário
        """
        print("Lista de usuários cadastrados")
        for user in users:
            # filter funciona como a cláusula WHERE
            user_profile = session.query(UserProfile).filter(UserProfile.id == user.id).first()

            output = f"""
            ID do Usuário: {user.id}
            Email: {user.email}
            Nome completo: {user_profile.first_name} {user_profile.last_name}
            """

            print(output)

        """
        No caso abaixo, utilizamos os atributos do tipo relationship para referenciar os
        dados que estão relacionados entre as models
        """
        print("Lista de usuários cadastrados")
        for user in users:
            output = f"""
                    ID do Usuário: {user.id}
                    Email: {user.email}
                    Nome completo: {user.profile.first_name} {user.profile.last_name}
                    """

            print(output)
