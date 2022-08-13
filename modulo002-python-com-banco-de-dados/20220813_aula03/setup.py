from database import engine, Base, session
from models import User, UserProfile, Post

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

    posts = [
        {"user_id": 1, "title": "A linguagem Python", "content": "Python é muito legal."},
        {"user_id": 1, "title": "A linguagem C++", "content": "C++ é muito poderoso."},
        {"user_id": 2, "title": "Docker", "content": "Docker é uma mão na roda."},
    ]

    # Só iremos inserir os dados se não houverem registros na tabela tb_users
    if len(result) == 0:
        for index, user_info in enumerate(users):

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

            for post_data in posts:
                if post_data.get("user_id") == user.id:
                    post = Post(
                        title=post_data.get("title"),
                        content=post_data.get("content")
                    )

                    # Adicionando o objeto Post à lista de posts da model User
                    user.posts.append(post)

                    # O objeto do tipo Post está sendo salvo na tabela de maneira indireta, pois ele foi adicionado
                    # a lista de posts do objeto user que faz referência a model Post
                    session.add(user)
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
