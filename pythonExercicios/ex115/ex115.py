from utils import funcs, validadores, pushpop
#todos = []
while True:
    funcs.menuzim()  # imprime o menu
    choice = input().strip()  # colhe a opção
    choice = validadores.validamenu(choice)  # trata o opção
    if choice == 3:
        funcs.titulo("ATÉ LOGO")
        break
    elif choice == 2:
        pushpop.pushfile()
        #todos.append(pushpop.push())
    elif choice == 1:
        pushpop.readfile()
        #funcs.titulo('PESSOAS CADASTRADAS')
        #for i in range(0, len(todos)):
        #    print(todos[i]['Nome'], end='')
        #    print(f'\t \t {todos[i]["Idade"]} anos')

