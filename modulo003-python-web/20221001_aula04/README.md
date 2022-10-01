Fonte dos dados: https://github.com/adaoduque/Brasileirao_Dataset

1) Iterar sobre a lista de jogos da rodada atual
2) Pegar, dentro da chave "clubs", os clubes das chaves "home" e "away"
3) Verificar se existem dados salvos relacionados aos nomes dos clubes que foram pegos
   - Se existirem, serão carregados. Se não, serão criados e depois carregados (método get_or_create das models)
4) Pegar, dentro do dicionário, as informaçoes sobre goals home e away, hour, date e stadium
5) Salvar uma nova model Match com os dados coletados (obj_round, obj_awayclub, obj_homeclub, goals_away, goals_home, date, hour, stadium)